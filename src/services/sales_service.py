"""Sales Service - Business logic for POS counter transactions."""

from datetime import date, datetime
import uuid
from typing import List

from src.core.exceptions import InsufficientPaymentError, StockValidationError
from src.models.sale import PaymentMethod, Sale, SaleItem, SaleStatus
from src.repositories.medicine_repository import IMedicineRepository
from src.repositories.sale_repository import ISaleRepository
from src.schemas.sale import CartItemDTO, CheckoutRequest, SaleReceiptResponse


class SalesService:
    """Orchestrates POS sales transactions, barcode scans, and atomic inventory reduction."""

    def __init__(self, medicine_repo: IMedicineRepository, sale_repo: ISaleRepository):
        self._medicine_repo = medicine_repo
        self._sale_repo = sale_repo

    async def scan_item(self, barcode: str, quantity: int = 1) -> CartItemDTO:
        """Validates stock quantity and expiry date for a scanned medicine item."""
        medicine = await self._medicine_repo.get_by_barcode(barcode)
        if not medicine:
            raise StockValidationError(f"Medicine with barcode '{barcode}' not found in catalog")

        if medicine.is_expired(today=date.today()):
            raise StockValidationError(
                f"Cannot sell '{medicine.trade_name}': Batch expired on {medicine.expiry_date}"
            )

        if medicine.stock_quantity < quantity:
            raise StockValidationError(
                f"Insufficient stock for '{medicine.trade_name}': Available {medicine.stock_quantity}, requested {quantity}"
            )

        line_total = round(medicine.selling_price * quantity, 2)
        return CartItemDTO(
            medicine_id=medicine.id,
            barcode=medicine.barcode,
            trade_name=medicine.trade_name,
            unit_price=medicine.selling_price,
            quantity=quantity,
            line_total=line_total,
        )

    async def finalize_sale(
        self,
        cashier_id: int,
        cart_items: List[CartItemDTO],
        checkout_data: CheckoutRequest,
    ) -> SaleReceiptResponse:
        """Atomically settles payment, decrements inventory stock, and logs sale invoice."""
        if not cart_items:
            raise StockValidationError("Cart is empty; cannot finalize sale")

        subtotal = sum(item.line_total for item in cart_items)
        discount_amount = 0.0
        net_total = round(subtotal - discount_amount, 2)

        if checkout_data.payment_method == PaymentMethod.CASH:
            if checkout_data.tendered_amount < net_total:
                raise InsufficientPaymentError(
                    f"Tendered amount {checkout_data.tendered_amount} EGP is less than bill total {net_total} EGP"
                )
            change_amount = round(checkout_data.tendered_amount - net_total, 2)
        else:
            change_amount = 0.0

        # Atomic inventory reduction
        for item in cart_items:
            success = await self._medicine_repo.decrement_stock_atomically(
                medicine_id=item.medicine_id, quantity=item.quantity
            )
            if not success:
                raise StockValidationError(f"Failed to reserve stock for medicine ID {item.medicine_id}")

        invoice_number = f"INV-{datetime.utcnow().strftime('%Y%m%d')}-{uuid.uuid4().hex[:6].upper()}"
        sale = Sale(
            invoice_number=invoice_number,
            cashier_id=cashier_id,
            subtotal=subtotal,
            discount_amount=discount_amount,
            net_total=net_total,
            status=SaleStatus.PAID,
            payment_method=checkout_data.payment_method,
        )
        saved_sale = await self._sale_repo.save(sale)

        return SaleReceiptResponse(
            id=saved_sale.id,
            invoice_number=saved_sale.invoice_number,
            sale_date=saved_sale.sale_date,
            subtotal=subtotal,
            discount_amount=discount_amount,
            net_total=net_total,
            tendered_amount=checkout_data.tendered_amount,
            change_amount=change_amount,
            payment_method=saved_sale.payment_method,
            status=saved_sale.status,
            items=cart_items,
        )

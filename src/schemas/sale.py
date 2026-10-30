"""Sales and POS schemas."""

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field
from src.models.sale import PaymentMethod, SaleStatus


class BarcodeScanRequest(BaseModel):
    barcode: str
    quantity: int = Field(1, ge=1)


class CartItemDTO(BaseModel):
    medicine_id: int
    barcode: str
    trade_name: str
    unit_price: float
    quantity: int
    line_total: float


class CheckoutRequest(BaseModel):
    payment_method: PaymentMethod = PaymentMethod.CASH
    tendered_amount: float = Field(..., gt=0)
    customer_name: Optional[str] = None
    customer_phone: Optional[str] = None


class SaleReceiptResponse(BaseModel):
    id: int
    invoice_number: str
    sale_date: datetime
    subtotal: float
    discount_amount: float
    net_total: float
    tendered_amount: float
    change_amount: float
    payment_method: PaymentMethod
    status: SaleStatus
    items: List[CartItemDTO]

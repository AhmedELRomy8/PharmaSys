"""Sales Router - POS Counter endpoints."""

from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.database import get_db_session
from src.core.exceptions import InsufficientPaymentError, StockValidationError
from src.repositories.medicine_repository import MedicineRepository
from src.repositories.sale_repository import SaleRepository
from src.schemas.sale import BarcodeScanRequest, CartItemDTO, CheckoutRequest, SaleReceiptResponse
from src.services.sales_service import SalesService

router = APIRouter(prefix="/sales", tags=["Sales & POS"])


def get_sales_service(session: AsyncSession = Depends(get_db_session)) -> SalesService:
    med_repo = MedicineRepository(session)
    sale_repo = SaleRepository(session)
    return SalesService(med_repo, sale_repo)


@router.post("/scan", response_model=CartItemDTO, status_code=status.HTTP_200_OK)
async def scan_barcode(
    payload: BarcodeScanRequest,
    service: SalesService = Depends(get_sales_service),
):
    """Scan a barcode and return validated item details for the POS cart."""
    try:
        return await service.scan_item(barcode=payload.barcode, quantity=payload.quantity)
    except StockValidationError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=exc.message)


@router.post("/checkout", response_model=SaleReceiptResponse, status_code=status.HTTP_201_CREATED)
async def checkout_sale(
    cart_items: List[CartItemDTO],
    checkout_data: CheckoutRequest,
    service: SalesService = Depends(get_sales_service),
):
    """Complete a sale, record the transaction, decrement stock atomically, and generate invoice."""
    try:
        # Default to cashier ID 1 for initial skeleton
        return await service.finalize_sale(
            cashier_id=1,
            cart_items=cart_items,
            checkout_data=checkout_data,
        )
    except InsufficientPaymentError as exc:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=exc.message)
    except StockValidationError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=exc.message)

"""Medicine catalog Router."""

from typing import List
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.database import get_db_session
from src.core.exceptions import StockValidationError
from src.repositories.medicine_repository import MedicineRepository
from src.schemas.medicine import MedicineCreate, MedicineResponse
from src.services.inventory_service import InventoryService

router = APIRouter(prefix="/medicines", tags=["Medicines & Inventory"])


def get_inventory_service(session: AsyncSession = Depends(get_db_session)) -> InventoryService:
    return InventoryService(MedicineRepository(session))


@router.post("/", response_model=MedicineResponse, status_code=status.HTTP_201_CREATED)
async def create_medicine(
    payload: MedicineCreate,
    service: InventoryService = Depends(get_inventory_service),
):
    """Add a new medicine to the catalog."""
    try:
        return await service.add_medicine(payload)
    except StockValidationError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=exc.message)


@router.get("/search", response_model=List[MedicineResponse], status_code=status.HTTP_200_OK)
async def search_medicines(
    q: str = Query(..., min_length=1, description="Search by trade name, generic name, or barcode"),
    service: InventoryService = Depends(get_inventory_service),
):
    """Search medicines in catalog."""
    return await service.search_catalog(q)

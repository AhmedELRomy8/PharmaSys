"""Inventory Service - Business logic for medicine catalog and stock monitoring."""

from typing import List
from src.core.exceptions import StockValidationError
from src.models.medicine import Medicine
from src.repositories.medicine_repository import IMedicineRepository
from src.schemas.medicine import MedicineCreate, MedicineResponse


class InventoryService:
    """Manages medicine catalog items, low-stock threshold monitoring, and expiry checks."""

    def __init__(self, medicine_repo: IMedicineRepository):
        self._medicine_repo = medicine_repo

    async def add_medicine(self, medicine_data: MedicineCreate) -> MedicineResponse:
        existing = await self._medicine_repo.get_by_barcode(medicine_data.barcode)
        if existing:
            raise StockValidationError(f"Barcode '{medicine_data.barcode}' is already assigned to {existing.trade_name}")

        medicine = Medicine(**medicine_data.model_dump())
        saved = await self._medicine_repo.save(medicine)
        return MedicineResponse.model_validate(saved)

    async def search_catalog(self, query: str) -> List[MedicineResponse]:
        medicines = await self._medicine_repo.search(query)
        return [MedicineResponse.model_validate(med) for med in medicines]

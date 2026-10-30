"""Medicine repository interface and implementation."""

from abc import ABC, abstractmethod
from typing import List, Optional
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.medicine import Medicine


class IMedicineRepository(ABC):
    """Interface contract for Medicine data access."""

    @abstractmethod
    async def get_by_id(self, medicine_id: int) -> Optional[Medicine]:
        pass

    @abstractmethod
    async def get_by_barcode(self, barcode: str) -> Optional[Medicine]:
        pass

    @abstractmethod
    async def search(self, query: str) -> List[Medicine]:
        pass

    @abstractmethod
    async def save(self, medicine: Medicine) -> Medicine:
        pass

    @abstractmethod
    async def decrement_stock_atomically(self, medicine_id: int, quantity: int) -> bool:
        pass


class MedicineRepository(IMedicineRepository):
    """Concrete SQLAlchemy implementation of Medicine repository."""

    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_by_id(self, medicine_id: int) -> Optional[Medicine]:
        result = await self._session.execute(select(Medicine).where(Medicine.id == medicine_id))
        return result.scalar_one_or_none()

    async def get_by_barcode(self, barcode: str) -> Optional[Medicine]:
        result = await self._session.execute(select(Medicine).where(Medicine.barcode == barcode))
        return result.scalar_one_or_none()

    async def search(self, query: str) -> List[Medicine]:
        stmt = select(Medicine).where(
            (Medicine.trade_name.ilike(f"%{query}%")) |
            (Medicine.generic_name.ilike(f"%{query}%")) |
            (Medicine.barcode == query)
        )
        result = await self._session.execute(stmt)
        return list(result.scalars().all())

    async def save(self, medicine: Medicine) -> Medicine:
        self._session.add(medicine)
        await self._session.commit()
        await self._session.refresh(medicine)
        return medicine

    async def decrement_stock_atomically(self, medicine_id: int, quantity: int) -> bool:
        medicine = await self.get_by_id(medicine_id)
        if not medicine or medicine.stock_quantity < quantity:
            return False
        medicine.stock_quantity -= quantity
        await self._session.commit()
        return True

"""Sale repository interface and implementation."""

from abc import ABC, abstractmethod
from typing import Optional
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.sale import Sale


class ISaleRepository(ABC):
    """Interface contract for Sale transactions."""

    @abstractmethod
    async def get_by_id(self, sale_id: int) -> Optional[Sale]:
        pass

    @abstractmethod
    async def get_by_invoice(self, invoice_number: str) -> Optional[Sale]:
        pass

    @abstractmethod
    async def save(self, sale: Sale) -> Sale:
        pass


class SaleRepository(ISaleRepository):
    """Concrete SQLAlchemy implementation of Sale repository."""

    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_by_id(self, sale_id: int) -> Optional[Sale]:
        result = await self._session.execute(select(Sale).where(Sale.id == sale_id))
        return result.scalar_one_or_none()

    async def get_by_invoice(self, invoice_number: str) -> Optional[Sale]:
        result = await self._session.execute(select(Sale).where(Sale.invoice_number == invoice_number))
        return result.scalar_one_or_none()

    async def save(self, sale: Sale) -> Sale:
        self._session.add(sale)
        await self._session.commit()
        await self._session.refresh(sale)
        return sale

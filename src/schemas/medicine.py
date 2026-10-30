"""Medicine catalog schemas."""

from datetime import date
from pydantic import BaseModel, Field
from src.models.medicine import DosageForm, PackageUnit


class MedicineBase(BaseModel):
    trade_name: str = Field(..., max_length=128)
    generic_name: str = Field(..., max_length=128)
    dosage_form: DosageForm
    package_unit: PackageUnit
    barcode: str = Field(..., max_length=64)
    selling_price: float = Field(..., gt=0)
    cost_price: float = Field(..., gt=0)
    stock_quantity: int = Field(..., ge=0)
    min_stock_threshold: int = Field(10, ge=0)
    expiry_date: date


class MedicineCreate(MedicineBase):
    pass


class MedicineResponse(MedicineBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True

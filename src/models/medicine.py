"""Medicine domain entity."""

from datetime import date
from enum import Enum
from sqlalchemy import Boolean, Date, Enum as SQLEnum, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from src.core.database import Base


class DosageForm(str, Enum):
    TABLET = "TABLET"
    CAPSULE = "CAPSULE"
    SYRUP = "SYRUP"
    SUSPENSION = "SUSPENSION"
    DROPS = "DROPS"
    OINTMENT = "OINTMENT"
    CREAM = "CREAM"
    INJECTION = "INJECTION"
    INHALER = "INHALER"


class PackageUnit(str, Enum):
    BOX = "BOX"
    STRIP = "STRIP"
    BOTTLE = "BOTTLE"
    TUBE = "TUBE"
    VIAL = "VIAL"
    SACHET = "SACHET"


class Medicine(Base):
    """Medicine entity representing items in the pharmacy inventory."""

    __tablename__ = "medicines"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    trade_name: Mapped[str] = mapped_column(String(128), index=True, nullable=False)
    generic_name: Mapped[str] = mapped_column(String(128), nullable=False)
    dosage_form: Mapped[DosageForm] = mapped_column(SQLEnum(DosageForm), nullable=False)
    package_unit: Mapped[PackageUnit] = mapped_column(SQLEnum(PackageUnit), nullable=False)
    barcode: Mapped[str] = mapped_column(String(64), unique=True, index=True, nullable=False)
    selling_price: Mapped[float] = mapped_column(Float, nullable=False)
    cost_price: Mapped[float] = mapped_column(Float, nullable=False)
    stock_quantity: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    min_stock_threshold: Mapped[int] = mapped_column(Integer, default=10, nullable=False)
    expiry_date: Mapped[date] = mapped_column(Date, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    def is_expired(self, today: date | None = None) -> bool:
        reference_date = today or date.today()
        return self.expiry_date <= reference_date

    def is_low_stock(self) -> bool:
        return self.stock_quantity <= self.min_stock_threshold

"""User domain entity."""

from enum import Enum
from sqlalchemy import Boolean, Enum as SQLEnum, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from src.core.database import Base


class UserRole(str, Enum):
    SUPER_ADMIN = "SUPER_ADMIN"
    ADMIN = "ADMIN"
    STAFF = "STAFF"


class User(Base):
    """User entity representing pharmacists and hospital administrators."""

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    full_name: Mapped[str] = mapped_column(String(128), nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    role: Mapped[UserRole] = mapped_column(SQLEnum(UserRole), default=UserRole.STAFF, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

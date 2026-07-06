from datetime import datetime
from enum import Enum

from sqlalchemy import DateTime, Enum as SQLEnum, ForeignKey, String, func,UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base

from typing import TYPE_CHECKING

from sqlalchemy.orm import relationship

if TYPE_CHECKING:
    from app.models.transaction import Transaction
    from app.models.user import User


class CategoryType(str, Enum):
    INCOME = "income"
    EXPENSE = "expense"


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(
        primary_key=True, 
            index=True
    )

    name: Mapped[str] = mapped_column(
        String(100),
        index=True,
        nullable=False,
    )

    type: Mapped[CategoryType] = mapped_column(
        SQLEnum(CategoryType),
        nullable=False,
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )
    
    user: Mapped["User"] = relationship(
    back_populates="categories",
    )

    transactions: Mapped[list["Transaction"]] = relationship(
    back_populates="category",
    cascade="all, delete-orphan",
    )
    
    __table_args__ = (
    UniqueConstraint(
        "user_id",
        "name",
        "type",
        name="uq_user_category_name_type",
    ),
)
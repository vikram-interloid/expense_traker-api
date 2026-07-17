from datetime import datetime
from typing import TYPE_CHECKING
import uuid
from sqlalchemy.dialects.postgresql import  UUID


from enum import Enum
from sqlalchemy import DateTime, Enum as SQLEnum, ForeignKey, String, func,UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column,relationship
from app.db.base import Base

if TYPE_CHECKING:
    from app.models.transaction import Transaction
    from app.models.user import User
class CategoryType(str, Enum):
    INCOME = "income"
    EXPENSE = "expense"
class Category(Base):
    __tablename__ = "categories"
    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True, 
        default=uuid.uuid4,
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

    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
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

from datetime import datetime

from sqlalchemy import DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base

from typing import TYPE_CHECKING

from sqlalchemy.orm import relationship

if TYPE_CHECKING:
    from app.models.category import Category
    from app.models.refresh_token import RefreshToken
    from app.models.transaction import Transaction


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    username: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        index=True,
        nullable=False,
    )

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        index=True,
        nullable=False,
    )

    password_hash: Mapped[str] = mapped_column(
        String(255),
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
    
    categories: Mapped[list["Category"]] = relationship(
    back_populates="user",
    cascade="all, delete-orphan",
    )

    transactions: Mapped[list["Transaction"]] = relationship(
    back_populates="user",
    cascade="all, delete-orphan",
    )

    refresh_tokens: Mapped[list["RefreshToken"]] = relationship(
    back_populates="user",
    cascade="all, delete-orphan",
    )
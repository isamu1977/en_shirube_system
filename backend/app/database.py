"""
Database configuration for Tarô de Raízes.

Provides async SQLAlchemy engine, session factory, and a declarative Base
for all ORM models. Also provides a synchronous engine for scripts like
the seed script that don't need async.
"""

import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

load_dotenv()

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+asyncpg://postgres:postgres@localhost:5432/en_shirube_system",
)

# Derive sync URL for scripts (seed, migrations) by swapping the driver
SYNC_DATABASE_URL = DATABASE_URL.replace("+asyncpg", "").replace(
    "postgresql://", "postgresql+psycopg2://"
)
if SYNC_DATABASE_URL.startswith("postgresql+psycopg2"):
    pass  # already correct
elif SYNC_DATABASE_URL.startswith("postgresql://"):
    SYNC_DATABASE_URL = SYNC_DATABASE_URL.replace(
        "postgresql://", "postgresql+psycopg2://"
    )

# --- Async engine (for FastAPI runtime) ---
async_engine = create_async_engine(DATABASE_URL, echo=False, future=True)

AsyncSessionLocal = sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

# --- Sync engine (for seed scripts, CLI tools) ---
sync_engine = create_engine(SYNC_DATABASE_URL, echo=False, future=True)

SyncSessionLocal = sessionmaker(bind=sync_engine, expire_on_commit=False)


class Base(DeclarativeBase):
    """Declarative base for all Tarô de Raízes ORM models."""

    pass


async def get_db() -> AsyncSession:
    """FastAPI dependency that yields an async database session."""
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()

from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Store the SQLite database file inside the backend folder.
BASE_DIR = Path(__file__).resolve().parent
DATABASE_URL = f"sqlite:///{BASE_DIR / 'romchi.db'}"

# SQLite needs this option so the same connection can be used safely.
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for all SQLAlchemy models.
Base = declarative_base()


def init_db() -> None:
    """Create all tables defined by the models."""
    # Import models here to ensure they are registered with SQLAlchemy.
    from models import Conversation  # noqa: F401

    Base.metadata.create_all(bind=engine)

from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Always point to the same SQLite file
DB_PATH = Path(__file__).resolve().parents[2] / "analytics.db"

engine = create_engine(
    f"sqlite:///{DB_PATH}",
    echo=False,
    future=True,
)

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
    future=True,
)

Base = declarative_base()
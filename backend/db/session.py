from typing import Generator
from .database import SessionLocal

def get_db() -> Generator:
    db = SessionLocal()  # 2
    try:
        yield db  # 3
    finally:
        db.close()
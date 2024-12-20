from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///travel_planner.db"

engine = create_engine(DATABASE_URL, echo=True)  # Set echo=True for SQL debugging
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    """Yield a new session for database interaction."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.db.models import Base, Trip
from lib.budget_manager import BudgetManager

@pytest.fixture
def session():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()
    Base.metadata.drop_all(engine)

def test_view_budget(session):
    trip = Trip(name="Test Trip", budget=1000)
    session.add(trip)
    session.commit()

    saved_trip = session.query(Trip).filter_by(name="Test Trip").first()
    assert saved_trip.budget == 1000

def test_update_budget(session):
    trip = Trip(name="Test Trip", budget=1000)
    session.add(trip)
    session.commit()

    trip.budget = 2000
    session.commit()

    updated_trip = session.query(Trip).filter_by(name="Test Trip").first()
    assert updated_trip.budget == 2000

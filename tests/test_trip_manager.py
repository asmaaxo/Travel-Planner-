import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.db.models import Base, Trip
from lib.trip_manager import TripManager

@pytest.fixture
def session():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()
    Base.metadata.drop_all(engine)

def test_create_trip(session):
    manager = TripManager(session)
    trip = Trip(name="Test Trip", budget=1000)
    session.add(trip)
    session.commit()

    saved_trip = session.query(Trip).filter_by(name="Test Trip").first()
    assert saved_trip is not None
    assert saved_trip.name == "Test Trip"
    assert saved_trip.budget == 1000

def test_update_trip(session):
    manager = TripManager(session)
    trip = Trip(name="Old Trip", budget=500)
    session.add(trip)
    session.commit()

    trip.name = "Updated Trip"
    session.commit()

    updated_trip = session.query(Trip).filter_by(name="Updated Trip").first()
    assert updated_trip is not None
    assert updated_trip.name == "Updated Trip"

def test_delete_trip(session):
    manager = TripManager(session)
    trip = Trip(name="Test Trip", budget=1000)
    session.add(trip)
    session.commit()

    session.delete(trip)
    session.commit()

    deleted_trip = session.query(Trip).filter_by(name="Test Trip").first()
    assert deleted_trip is None

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.db.models import Base, Trip, Destination
from lib.destination_manager import DestinationManager

@pytest.fixture
def session():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()
    Base.metadata.drop_all(engine)

def test_add_destination(session):
    trip = Trip(name="Test Trip", budget=1000)
    session.add(trip)
    session.commit()

    destination = Destination(trip_id=trip.id, name="Test Destination")
    session.add(destination)
    session.commit()

    saved_destination = session.query(Destination).filter_by(name="Test Destination").first()
    assert saved_destination is not None
    assert saved_destination.trip_id == trip.id

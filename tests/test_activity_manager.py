import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.db.models import Base, Trip, Destination, Activity
from lib.activity_manager import ActivityManager

@pytest.fixture
def session():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()
    Base.metadata.drop_all(engine)

def test_add_activity(session):
    trip = Trip(name="Test Trip", budget=1000)
    session.add(trip)
    session.commit()

    destination = Destination(trip_id=trip.id, name="Test Destination")
    session.add(destination)
    session.commit()

    activity = Activity(destination_id=destination.id, name="Test Activity")
    session.add(activity)
    session.commit()

    saved_activity = session.query(Activity).filter_by(name="Test Activity").first()
    assert saved_activity is not None
    assert saved_activity.destination_id == destination.id

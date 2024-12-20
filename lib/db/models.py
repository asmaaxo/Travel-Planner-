from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Trip(Base):
    __tablename__ = "trips"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    budget = Column(Float, default=0.0)

    destinations = relationship("Destination", back_populates="trip", cascade="all, delete-orphan")


class Destination(Base):
    __tablename__ = "destinations"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    trip_id = Column(Integer, ForeignKey("trips.id"), nullable=False)

    trip = relationship("Trip", back_populates="destinations")
    activities = relationship("Activity", back_populates="destination", cascade="all, delete-orphan")


class Activity(Base):
    __tablename__ = "activities"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    destination_id = Column(Integer, ForeignKey("destinations.id"), nullable=False)

    destination = relationship("Destination", back_populates="activities")

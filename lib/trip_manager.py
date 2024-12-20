from lib.db.models import Trip  # Import the Trip SQLAlchemy model
from sqlalchemy.orm import Session  # Import Session to type-hint the session

class TripManager:
    def __init__(self, session: Session):
        self.session = session

    def create_trip(self):
        """Create a new trip."""
        name = input("Enter trip name: ").strip()
        try:
            budget = float(input("Enter trip budget: "))
            trip = Trip(name=name, budget=budget)
            self.session.add(trip)  # Add the trip object to the session
            self.session.commit()  # Commit the changes to the database
            print(f"Trip '{name}' created successfully.")
        except Exception as e:
            self.session.rollback()  # Rollback in case of an error
            print(f"Error creating trip: {e}")

    def view_trips(self):
        """View all trips."""
        trips = self.session.query(Trip).all()  # Query all trips
        if not trips:
            print("No trips available.")
            return
        for trip in trips:
            print(f"Trip ID: {trip.id}, Name: {trip.name}, Budget: {trip.budget}")

    def update_trip(self):
        """Update a trip's details."""
        try:
            trip_id = int(input("Enter trip ID to update: "))
            trip = self.session.query(Trip).get(trip_id)  # Query the trip by ID
            if not trip:
                print("Trip not found.")
                return
            trip.name = input(f"Enter new name (current: {trip.name}): ").strip()
            trip.budget = float(input(f"Enter new budget (current: {trip.budget}): "))
            self.session.commit()
            print("Trip updated successfully.")
        except Exception as e:
            self.session.rollback()
            print(f"Error updating trip: {e}")

    def delete_trip(self):
        """Delete a trip."""
        try:
            trip_id = int(input("Enter trip ID to delete: "))
            trip = self.session.query(Trip).get(trip_id)
            if not trip:
                print("Trip not found.")
                return
            self.session.delete(trip)  # Delete the trip object
            self.session.commit()
            print("Trip deleted successfully.")
        except Exception as e:
            self.session.rollback()
            print(f"Error deleting trip: {e}")

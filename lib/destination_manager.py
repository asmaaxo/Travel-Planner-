from lib.db.models import Destination
from sqlalchemy.orm import Session

class DestinationManager:
    def __init__(self, session: Session):
        self.session = session

    def add_destination(self):
        trip_id = int(input("Enter Trip ID: "))
        name = input("Enter Destination Name: ").strip()
        try:
            destination = Destination(name=name, trip_id=trip_id)
            self.session.add(destination)
            self.session.commit()
            print(f"Destination '{name}' added to trip ID {trip_id}.")
        except Exception as e:
            self.session.rollback()
            print(f"Error adding destination: {e}")

    def view_destinations(self):
        trip_id = int(input("Enter Trip ID: "))
        destinations = self.session.query(Destination).filter(Destination.trip_id == trip_id).all()
        if not destinations:
            print(f"No destinations found for trip ID {trip_id}.")
            return
        for destination in destinations:
            print(f"Destination ID: {destination.id}, Name: {destination.name}")

    def update_destination(self):
        destination_id = int(input("Enter Destination ID to update: "))
        destination = self.session.query(Destination).get(destination_id)
        if not destination:
            print("Destination not found.")
            return
        try:
            new_name = input(f"Enter new name (current: {destination.name}): ").strip()
            destination.name = new_name
            self.session.commit()
            print("Destination updated successfully.")
        except Exception as e:
            self.session.rollback()
            print(f"Error updating destination: {e}")

    def delete_destination(self):
        destination_id = int(input("Enter Destination ID to delete: "))
        destination = self.session.query(Destination).get(destination_id)
        if not destination:
            print("Destination not found.")
            return
        try:
            self.session.delete(destination)
            self.session.commit()
            print("Destination deleted successfully.")
        except Exception as e:
            self.session.rollback()
            print(f"Error deleting destination: {e}")

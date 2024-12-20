from sqlalchemy.orm import Session
from lib.db.models import Activity

class ActivityManager:
    def __init__(self, session):
        self.session = session

    def add_activity(self):
        """Add a new activity to a destination."""
        destination_id = int(input("Enter Destination ID: "))
        name = input("Enter Activity Name: ").strip()
        try:
            activity = Activity(name=name, destination_id=destination_id)
            self.session.add(activity)
            self.session.commit()
            print(f"Activity '{name}' added to destination ID {destination_id}.")
        except Exception as e:
            self.session.rollback()
            print(f"Error adding activity: {e}")

    def view_activities(self):
        """View all activities for a specific destination."""
        destination_id = int(input("Enter Destination ID: "))
        activities = self.session.query(Activity).filter(Activity.destination_id == destination_id).all()
        if not activities:
            print(f"No activities found for destination ID {destination_id}.")
            return
        for activity in activities:
            print(f"Activity ID: {activity.id}, Name: {activity.name}")

    def update_activity(self):
        """Update an activity's details."""
        activity_id = int(input("Enter Activity ID to update: "))
        activity = self.session.query(Activity).get(activity_id)
        if not activity:
            print("Activity not found.")
            return
        try:
            new_name = input(f"Enter new name (current: {activity.name}): ").strip()
            activity.name = new_name
            self.session.commit()
            print("Activity updated successfully.")
        except Exception as e:
            self.session.rollback()
            print(f"Error updating activity: {e}")

    def delete_activity(self):
        """Delete an activity."""
        activity_id = int(input("Enter Activity ID to delete: "))
        activity = self.session.query(Activity).get(activity_id)
        if not activity:
            print("Activity not found.")
            return
        try:
            self.session.delete(activity)
            self.session.commit()
            print("Activity deleted successfully.")
        except Exception as e:
            self.session.rollback()
            print(f"Error deleting activity: {e}")

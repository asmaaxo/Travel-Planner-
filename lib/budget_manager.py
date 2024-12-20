from sqlalchemy.orm import Session
from lib.db.models import Trip

class BudgetManager:
    def __init__(self, session):
        self.session = session

    def view_budget(self):
        """View the budget of a trip."""
        trip_id = int(input("Enter Trip ID: "))
        trip = self.session.query(Trip).get(trip_id)
        if not trip:
            print("Trip not found.")
            return
        print(f"Trip '{trip.name}' has a budget of {trip.budget}.")

    def update_budget(self):
        """Update the budget of a trip."""
        trip_id = int(input("Enter Trip ID: "))
        trip = self.session.query(Trip).get(trip_id)
        if not trip:
            print("Trip not found.")
            return
        try:
            new_budget = float(input(f"Enter new budget (current: {trip.budget}): "))
            trip.budget = new_budget
            self.session.commit()
            print("Budget updated successfully.")
        except Exception as e:
            self.session.rollback()
            print(f"Error updating budget: {e}")

    def track_expenses(self):
        """Track expenses for a trip."""
        trip_id = int(input("Enter Trip ID: "))
        trip = self.session.query(Trip).get(trip_id)
        if not trip:
            print("Trip not found.")
            return
        try:
            expense = float(input("Enter expense amount: "))
            trip.budget -= expense
            self.session.commit()
            print(f"Expense of {expense} deducted. Remaining budget: {trip.budget}.")
        except Exception as e:
            self.session.rollback()
            print(f"Error tracking expenses: {e}")

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from lib.trip_manager import TripManager
from lib.destination_manager import DestinationManager
from lib.activity_manager import ActivityManager
from lib.budget_manager import BudgetManager
from lib.db.models import Base


# Initialize Database and Session
engine = create_engine("sqlite:///travel_planner.db", echo=False)
Session = sessionmaker(bind=engine)
session = Session()


def main_menu():
    """Main menu for the Travel Planner CLI."""
    trip_manager = TripManager(session)
    destination_manager = DestinationManager(session)
    activity_manager = ActivityManager(session)
    budget_manager = BudgetManager(session)

    while True:
        print("\n=== Travel Planner CLI ===")
        print("1. Create Trip")
        print("2. View Trips")
        print("3. Update Trip")
        print("4. Delete Trip")
        print("5. View Budget")
        print("6. Update Budget")
        print("7. Track Expenses")
        print("8. Add Destination to Trip")
        print("9. View Destinations for a Trip")
        print("10. Update Destination")
        print("11. Delete Destination")
        print("12. Add Activity to Destination")
        print("13. View Activities for a Destination")
        print("14. Update Activity")
        print("15. Delete Activity")
        print("16. Exit")

        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            trip_manager.create_trip()
        elif choice == 2:
            trip_manager.view_trips()
        elif choice == 3:
            trip_manager.update_trip()
        elif choice == 4:
            trip_manager.delete_trip()
        elif choice == 5:
            budget_manager.view_budget()
        elif choice == 6:
            budget_manager.update_budget()
        elif choice == 7:
            budget_manager.track_expenses()
        elif choice == 8:
            destination_manager.add_destination()
        elif choice == 9:
            destination_manager.view_destinations()
        elif choice == 10:
            destination_manager.update_destination()
        elif choice == 11:
            destination_manager.delete_destination()
        elif choice == 12:
            activity_manager.add_activity()
        elif choice == 13:
            activity_manager.view_activities()
        elif choice == 14:
            activity_manager.update_activity()
        elif choice == 15:
            activity_manager.delete_activity()
        elif choice == 16:
            print("Exiting Travel Planner. Goodbye!")
            session.close()
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    # Ensure database tables are created
    Base.metadata.create_all(engine)
    main_menu()

Travel Planning App
A command-line interface (CLI) application to help users plan and organize their trips efficiently.

Features
Trip Management: Create, view, update, and delete trips.
Destination Planning: Add and manage destinations within each trip.
Activity Management: Organize activities for each destination.
Budget Tracking: Set budgets and track expenses for trips.
Itinerary Overview: View a day-by-day itinerary combining destinations and activities.
Installation
Clone the repository:

Copy code
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install the required packages:

Copy code
pip install -r requirements.txt
Set up the database:

Initialize the database using Alembic:

Copy code
alembic upgrade head
If Alembic is not initialized, set it up:

Copy code
alembic init migrations
Configure alembic.ini to point to your database.

Generate initial migration:

Copy code
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head
Usage
Run the CLI application:

Copy code
python cli.py
Follow the on-screen menu to manage trips, destinations, activities, and budgets.

Project Structure
cli.py: Main entry point for the CLI application.
models.py: Contains SQLAlchemy ORM models for the database.
connection.py: Handles database connection setup.
migrations/: Directory for Alembic database migrations.
lib/: Contains modules for managing trips, destinations, activities, and budgets.
Dependencies
Python 3.7+
SQLAlchemy
Alembic
Other dependencies listed in requirements.txt
Contributing
Fork the repository.

Create a new branch:

Copy code
git checkout -b feature/your-feature-name
Make your changes and commit them:

Copy code
git commit -m "Add your message here"
Push to your fork:

Copy code
git push origin feature/your-feature-name
Create a pull request.

video link: https://www.awesomescreenshot.com/video/34843670?key=b8aa20adce67f043ca142d6dc11316b1
slides link: https://docs.google.com/presentation/d/13DIg9FENMBmWE7liJXo0bT0A9_RAWPONXX_G7slMdAI/edit#slide=id.p3
License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
This project utilizes SQLAlchemy for ORM and Alembic for database migrations.

For more information on setting up similar projects, refer to:

Sample setup for SQLAlchemy and Alembic
Building a Python Database Application with SQLAlchemy and Alembic

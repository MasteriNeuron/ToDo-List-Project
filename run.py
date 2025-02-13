"""
This is the main entry point for the Flask application.
It handles application initialization, database setup, and server startup.
"""

# Import the application factory function and database instance from the app package
from app import create_app, db

# Initialize the Flask application using the factory function
# This creates the app instance with all configurations, blueprints, and extensions
app = create_app()

# Define a custom Flask CLI command to create database tables
@app.cli.command("create-db")
def create_db():
    """
    Purpose: Creates all database tables defined in the models
    Outcome: 
    - Creates SQL tables for User and Task models if they don't exist
    - Prints confirmation message when successful
    - Usage: Run 'flask create-db' in terminal
    """
    db.create_all()  # SQLAlchemy method to create tables
    print("Database tables created!")  # CLI feedback

# Main execution block - only runs when file is executed directly
if __name__ == '__main__':
    """
    Purpose: Start the Flask development server
    Outcome:
    - Starts the WSGI server on default port 5000
    - Enables debug mode if FLASK_ENV=development
    - Accessible at http://localhost:5000
    """
    app.run(host='0.0.0.0',port=8080)  # Start the Flask application server

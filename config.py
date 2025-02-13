import os
from datetime import timedelta

# Get the absolute path of the current directory (where this script is located)
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    """
    Purpose:
    This class defines the configuration settings for the application.

    Outcome:
    - Sets up the database URI, either from an environment variable or as a fallback to a local SQLite database.
    - Disables SQLAlchemy event tracking to improve performance.
    - Configures JWT (JSON Web Token) settings for authentication security.
    """

    # Define the database URI, using an environment variable if available,
    # otherwise defaulting to an SQLite database file named 'todo.db' in the current directory.
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'todo.db')

    # Disable modification tracking feature of SQLAlchemy to reduce overhead.
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Secret key for JWT authentication, retrieved from environment variables.
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')

    # Set JWT access token expiration time to 1 hour.
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flasgger import Swagger
from config import Config

db = SQLAlchemy()
jwt = JWTManager()
migrate = Migrate()
swagger = Swagger()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

        # Add Swagger configuration
    app.config['SWAGGER'] = {
        'title': 'ToDo API',
        'uiversion': 3,
        'securityDefinitions': {
            'BearerAuth': {
                'type': 'apiKey',
                'name': 'Authorization',
                'in': 'header'
            }
        },
        'security': [
            {'BearerAuth': []}
        ]
    }

    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)
    swagger.init_app(app)

    # Import models to ensure they are registered with SQLAlchemy
    from app.models import User, Task

    # Create tables if they don't exist (for development only)
    with app.app_context():
        db.create_all()

    # Register blueprints
    from app.routes import api_blueprint
    app.register_blueprint(api_blueprint)

    return app
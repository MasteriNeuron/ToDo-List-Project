from flask import Blueprint
from app.resources.auth import RegistrationResource, AuthResource, LogoutResource
from app.resources.tasks import TaskResource, TaskDetailResource

api_blueprint = Blueprint('api', __name__)

# Authentication routes
api_blueprint.add_url_rule('/register', view_func=RegistrationResource.as_view('register'))
api_blueprint.add_url_rule('/login', view_func=AuthResource.as_view('login'))
api_blueprint.add_url_rule('/logout', view_func=LogoutResource.as_view('logout'))

# Task routes
api_blueprint.add_url_rule('/tasks', view_func=TaskResource.as_view('tasks'))
api_blueprint.add_url_rule('/tasks/<int:task_id>', view_func=TaskDetailResource.as_view('task_detail'))
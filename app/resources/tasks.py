
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import request
from app.models import Task, User, db
from datetime import datetime

task_parser = reqparse.RequestParser()
task_parser.add_argument('title', type=str, required=True)
task_parser.add_argument('description', type=str)
task_parser.add_argument('due_date', type=str)
task_parser.add_argument('due_time', type=str)
task_parser.add_argument('priority', type=str)
task_parser.add_argument('status', type=str)

class TaskResource(Resource):
    @jwt_required()
    def post(self):
        """ Create new task
        ---
        tags:
          - tasks
        security:
          - BearerAuth: []
        parameters:
          - in: body
            name: body
            required: true
            schema:
              type: object
              required:
                - title
              properties:
                title:
                  type: string
                description:
                  type: string
                due_date:
                  type: string
                due_time:
                  type: string
                priority:
                  type: string

        responses:
          201:
            description: Task created
        """
        args = task_parser.parse_args()
        user_id = int(get_jwt_identity())
        try:
          due_date = datetime.strptime(args['due_date'], '%Y-%m-%d').date()
          due_time = datetime.strptime(args['due_time'], '%H:%M:%S').time()


        except ValueError:
            return {'message': 'Invalid date or time format. Use ISO format'}, 400
        task = Task(
            title=args['title'],
            description=args['description'],
            due_date=due_date,
            due_time=due_time,
            priority=args.get('priority', 'medium'),
            user_id=user_id
        )
        db.session.add(task)
        db.session.commit()
        return task.to_dict(), 201

    @jwt_required()
    def get(self):
        """ Get all tasks for current user
        ---
        tags:
          - tasks
        security:
          - BearerAuth: []
        responses:
          200:
            description: List of tasks
        """
        user_id = get_jwt_identity()
        tasks = Task.query.filter_by(user_id=user_id).all()
        return [task.to_dict() for task in tasks]

class TaskDetailResource(Resource):
    @jwt_required()
    def get(self, task_id):
        """ Get single task
        ---
        tags:
          - tasks
        security:
          - BearerAuth: []
        parameters:
          - in: path
            name: task_id
            required: true
            type: integer
        responses:
          200:
            description: Task details
          404:
            description: Task not found
        """
        user_id = get_jwt_identity()
        task = Task.query.filter_by(id=task_id, user_id=user_id).first_or_404()
        return task.to_dict()

    @jwt_required()
    def put(self, task_id):
        """ Update task
        ---
        tags:
          - tasks
        security:
          - BearerAuth: []
        parameters:
          - in: path
            name: task_id
            required: true
            type: integer
          - in: body
            name: body
            schema:
              type: object
              properties:
                title:
                  type: string
                description:
                  type: string
                due_date:
                  type: string
                due_time:
                  type: string
                priority:
                  type: string
                status:
                  type: string
        responses:
          200:
            description: Task updated
          404:
            description: Task not found
        """
        task = Task.query.filter_by(id=task_id, user_id=get_jwt_identity()).first_or_404()
        args = task_parser.parse_args()
        if args['title']:
            task.title = args['title']
        if args['description']:
            task.description = args['description']
        if args['due_date'] and args['due_time']:
            try:
                task.due_date = datetime.fromisoformat(args['due_date'] + 'T' + args['due_time'])
            except ValueError:
                return {'message': 'Invalid date or time format. Use ISO format'}, 400
        if args['priority']:
            task.priority = args['priority']
        if args['status']:
            task.status = args['status']
        db.session.commit()
        return task.to_dict()

    @jwt_required()
    def delete(self, task_id):
        """
        Delete task
        ---
        tags:
          - tasks
        security:
          - BearerAuth: []
        parameters:
          - in: path
            name: task_id
            required: true
            type: integer
        responses:
          204:
            description: Task deleted
          404:
            description: Task not found
        """
        task = Task.query.filter_by(
            id=task_id,
            user_id=get_jwt_identity()
        ).first_or_404()
        
        db.session.delete(task)
        db.session.commit()
        return '', 204


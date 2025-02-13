from flask_restful import Resource
from flask import request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.models import User
from app import db
from app.utils.security import hash_password, check_password

class RegistrationResource(Resource):
    def post(self):
        """ User registration endpoint
        ---
        tags:
          - auth
        parameters:
          - in: body
            name: body
            required: true
            schema:
              type: object
              required:
                - username
                - email
                - password
              properties:
                username:
                  type: string
                email:
                  type: string
                  format: email
                password:
                  type: string
        responses:
          201:
            description: User created successfully
          400:
            description: Username or email already exists
        """
        data = request.get_json()
        if User.query.filter_by(username=data['username']).first():
            return {'message': 'Username already exists'}, 400
        if User.query.filter_by(email=data['email']).first():
            return {'message': 'Email already exists'}, 400
        user = User(username=data['username'], email=data['email'])
        user.set_password(data['password'])
        db.session.add(user)
        db.session.commit()
        return {'message': 'User created successfully'}, 201

class AuthResource(Resource):
    def post(self):
        """ User login endpoint
        ---
        tags:
          - auth
        parameters:
          - in: body
            name: body
            required: true
            schema:
              type: object
              required:
                - username
                - email
                - password
              properties:
                username:
                  type: string
                email:
                  type: string
                  format: email
                password:
                  type: string
        responses:
          200:
            description: Login successful
            schema:
              type: object
              properties:
                access_token:
                  type: string
          401:
            description: Invalid credentials
        """
        username = request.json.get('username')
        password = request.json.get('password')
        user = User.query.filter_by(username=username).first()
        if not user or not user.check_password(password):
            return {'message': 'Invalid credentials'}, 401
        access_token = create_access_token(identity=str(user.id))
        return {'access_token': access_token}, 200


class LogoutResource(Resource):
    @jwt_required()
    def post(self):
        """ User logout endpoint
        ---
        tags:
          - auth
        security:
          - BearerAuth: []
        responses:
          200:
            description: Successfully logged out
        """
        return {'message': 'Successfully logged out'}, 200


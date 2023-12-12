from flask import request
from flask_jwt_extended import create_access_token
from flask_restful import Resource
from model.models import Users
from model import bcrypt

# An API to handle login of a user
class Login(Resource):
    def post(self):
        # Getting user credentials from request data (email and password)
        email = request.json.get('email')
        password = request.json.get('password')
        
        # Validating if email, password exists, if not raising exceptions
        if email is None or len(email) == 0:
            raise ValueError("Email is required to login!")
        
        if password is None or len(password) == 0:
            raise ValueError("Password is required to login!")
        
        if len(password) < 5:
            raise ValueError("Password length should be greater than 5!")
        
        # Getting the User from MySQL DB using email
        user = Users.query.filter_by(email=email).first()
        
        # If the User does not exists or if the password doesn't match, raising exception
        if user is None or not bcrypt.check_password_hash(user.password, password):
            raise ValueError("Invalid email or password")
        
        # Creating an access token and returning it with a 200 status code
        access_token = create_access_token(identity=user.id)
        return {'message': 'User logged in successfully!!', 'access_token': access_token}, 200

from flask import request
from flask_jwt_extended import create_access_token
from flask_restful import Resource
from model.models import Users
from model import db, bcrypt

# An API to handle user registration
class Register(Resource):
    
    def post(self):
        
        # Getting user credentials from request data (email and password)
        name = request.json.get('name')
        email = request.json.get('email')
        password = request.json.get('password')
        
        # Validating if name, email and password exists, if not raising exceptions
        if name is None or len(name) == 0:
            raise ValueError("Name is required to register!")
        
        if email is None or len(email) == 0:
            raise ValueError("Email is required to register!")
        
        if password is None or len(password) == 0:
            raise ValueError("Password is required to register!")
        
        if len(password) < 5:
            raise ValueError("Password length should be greater than 5!")
        
        # Hashing the password given by the User and saving the User to DB
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8') 
        user = Users(name, email, hashed_password)

        try:
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise ValueError("User with this email already exists!")
        
        # Creating an access token for the user and returning it with a 200 status code
        access_token = create_access_token(identity=user.id)
        return {'message': "User successfully registered!", 'access_token': access_token}, 200

from model import app
from flask_restful import Api
from api.predictionapi import Predictions
from api.loginapi import Login
from api.registerapi import Register
from flask import jsonify

api = Api(app)

#Calling the API endpoint to take the new tweet and predict on it
api.add_resource(Predictions, '/model/predict/<string:newTweet>')

#Calling the API endpoint to register new user
api.add_resource(Register, '/user/register')

#Calling the API endpoint to login the user
api.add_resource(Login, '/user/login')

# Handling the exceptions thrown by the APIs gracefully
@app.errorhandler(ValueError)
def handle_value_error(e):
    return jsonify(error = str(e)), 500

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000)
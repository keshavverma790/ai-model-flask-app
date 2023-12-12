from model.models import Results
from ai_model_operations.loadmodel import load_models
from ai_model_operations.preprocess import preprocess
from model import db
from flask_restful import Resource
from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

# An API to serve the AI model
class Predictions(Resource):
    
    # Using jwt_required decorator to authorize this end point
    @jwt_required()
    def post(self, newTweet):
        current_user_id = get_jwt_identity()
        
        # If the current user id does not exists returning a status code 401
        # Although the flow won't reach here if there is no access token, this is an extra check
        if current_user_id is None:
             return jsonify(message = "User not authorized to access this resource"), 401
        
        #appending the tweet to a list because the preprocess function only takes list as parameter
        tweetList = []
        tweetList.append(newTweet)
        
        #loading the vectoriser and model
        vectoriser, model = load_models()
        
        #preprocessing and vectorising the new tweet for prediction
        tweet = preprocess(tweetList)
        tweetdata = vectoriser.transform(tweet)
        
        #prediction for the new tweet
        predictions = model.predict(tweetdata).tolist()
        
        #saving the predictions to results table in db and raising an exception if something goes wrong
        if(predictions[0] == 0):
            result = "negative"
        else:
            result = "positive"
        model_prediction = Results(newTweet, result, current_user_id)
        try:
            db.session.add(model_prediction)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise ValueError("Something went wrong when saving the results to Database!")

        #returning the response to the user
        return jsonify(newTweet + " is " + result + "!")
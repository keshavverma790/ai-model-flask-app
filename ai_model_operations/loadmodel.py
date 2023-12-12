import os
import pickle

# A method to load the models from pickle file
def load_models():  
       
    vectoriser_path = os.getenv('VECTORIZER_PATH', '/path/to/vectoriser.pickle')
    lr_model_path = os.getenv('LR_MODEL_PATH', '/path/to/Sentiment-LR.pickle')
       
    # Load the vectoriser.
    file = open(vectoriser_path, 'rb')
    vectoriser = pickle.load(file)
    file.close()
    
    # Load the LR Model.
    file = open(lr_model_path, 'rb')
    LRmodel = pickle.load(file)
    file.close()
    
    return vectoriser, LRmodel
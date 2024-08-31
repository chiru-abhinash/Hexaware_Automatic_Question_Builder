# utils/ai_models.py

import pickle

def load_model(model_path):
    """
    Loads a pre-trained AI model.
    """
    with open(model_path, 'rb') as model_file:
        model = pickle.load(model_file)
    return model

def predict(model, input_data):
    """
    Predicts the output based on the input data using the loaded model.
    """
    return model.predict(input_data)

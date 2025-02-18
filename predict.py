import pickle
import numpy as np

# Load pre-trained models
flood_model = pickle.load(open("models/flood_model.pkl", "rb"))
wildfire_model = pickle.load(open("models/wildfire_model.pkl", "rb"))
earthquake_model = pickle.load(open("models/earthquake_model.pkl", "rb"))

def predict_disaster(disaster_type, location_data):
    if disaster_type == "flood":
        return flood_model.predict(np.array([location_data]).reshape(1, -1))
    elif disaster_type == "wildfire":
        return wildfire_model.predict(np.array([location_data]).reshape(1, -1))
    elif disaster_type == "earthquake":
        return earthquake_model.predict(np.array([location_data]).reshape(1, -1))
    else:
        return "Invalid disaster type."

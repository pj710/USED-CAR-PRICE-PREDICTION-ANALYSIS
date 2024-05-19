"""
Author: Josiah Gordor

"""
import joblib
import pandas as pd

class Estimator:
    def __init__(self, model):
        self.model = model 

    def estimate_price(self, car):
        
        car_features = car.get_features()

        # Convert to DataFrame
        car_features_df = pd.DataFrame([car_features], columns=['brand', 'model', 'year', 'mileage', 'color', 'state'])
        
        predicted_price = self.model.predict(car_features_df)
        
        return predicted_price



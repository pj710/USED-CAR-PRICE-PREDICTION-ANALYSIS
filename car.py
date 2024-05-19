"""
Author: Josiah Gordor

"""

class Car:
    def __init__(self, brand, model, year,mileage, color, state):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
        self.color = color
        self.state = state

    def get_features(self):
        # Convert the Car instance data into a format suitable for prediction
        return [self.brand, self.model, self.year, self.mileage, self.color, self.state]
        

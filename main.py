"""
Author: Josiah Gordor

"""
from car import Car
from estimator import Estimator
import joblib
from plotter import CarExploratoryAnalysis

def main():
    # Load the pre-trained model
    model= joblib.load("motovalue_model.joblib")
    estimator = Estimator(model)

    # Request user input
    print("Please enter the car's details:")
    brand = input("Brand: ")
    model = input("Model: ")
    year = int(input("Year: "))
    mileage = float(input("Mileage: "))
    color = input("Color: ")
    state = input("State: ")

    # Create a Car instance
    car = Car(brand, model, year, mileage, color, state)

    # Make a prediction
    predicted_price = estimator.estimate_price(car)[0]
    
    # Output the predicted price
    print(f"Predicted price for this car: ${predicted_price:,.2f}")
    
    # Visualize car data
    analysis = CarExploratoryAnalysis()  
    analysis.plot_price_distribution()
    analysis.plot_price_by_feature('brand')  
    analysis.plot_price_by_feature('state')

if __name__ == "__main__":
    main()
    

"""
Author: Josiah Gordor

"""

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_squared_error

# Load the dataset
df = pd.read_csv('data/USA_cars_datasets.csv')

# Select features and target
features = ['brand', 'model', 'year','mileage', 'color', 'state']
target = 'price'

X = df[features]
y = df[target]

# Split the dataset into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Preprocessing data
categorical_transformer = Pipeline(steps=[
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer(
    transformers=[
        ('cat', categorical_transformer, ['brand', 'model', 'color', 'state'])
    ])

# Create the linear regression model
model = Pipeline(steps=[('preprocessor', preprocessor),
                        ('model',LinearRegression())])


# Train the model
model.fit(X_train, y_train)


# Predict the prices
y_pred = model.predict(X_test)


# Save the model for later use in estimator
import joblib
joblib.dump(model, 'motovalue_model.joblib')

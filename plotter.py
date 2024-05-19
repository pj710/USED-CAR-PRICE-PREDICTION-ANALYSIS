"""
Author: Josiah Gordor

"""

import pandas as pd
import matplotlib.pyplot as plt


class CarExploratoryAnalysis:
    def __init__(self, dataset_path='data/USA_cars_datasets.csv'):
        
        self.dataset = pd.read_csv(dataset_path)

        self.dataset['year'] = pd.to_datetime(self.dataset['year'], format='%Y')
    
    def plot_price_distribution(self):
        plt.figure(figsize=(10, 6))
        self.dataset['price'].hist(bins=50, color='blue', alpha=0.7)
        plt.title('Car Price Distribution')
        plt.xlabel('Price')
        plt.ylabel('Number of Cars')
        plt.grid(axis='y')
        plt.show()

    def plot_price_by_feature(self, feature, top_n=10):
        if feature not in self.dataset.columns:
            print(f"The feature '{feature}' is not in the dataset.")
            return
        self.dataset['year'] = pd.to_datetime(self.dataset['year'], format='%Y')

        # Calculate the mean price for each category within the feature
        mean_price = self.dataset.groupby(feature)['price'].mean().nlargest(top_n)
        top_categories = mean_price.index.tolist()

        # Filter the dataset to include only the top categories based on the mean price
        data_to_plot = self.dataset[self.dataset[feature].isin(top_categories)]

        # Generate the plot
        plt.figure(figsize=(10, 6))
        if data_to_plot[feature].dtype == 'object':
            # For categorical data: create a bar chart
            sorted_data = data_to_plot.groupby(feature)['price'].mean().loc[top_categories]
            sorted_data.plot(kind='bar', color='skyblue', alpha=0.7)
            plt.ylabel('General Average Price')
        else:
            # For numeric data: create a scatter plot
            plt.scatter(data_to_plot[feature], data_to_plot['price'])
            plt.ylabel('Price')
            
        plt.xlabel(feature.capitalize())
        plt.title(f'Top {top_n} {feature.capitalize()} by Average Price')
        plt.xticks(rotation=45) 
        plt.tight_layout() 
        plt.show()


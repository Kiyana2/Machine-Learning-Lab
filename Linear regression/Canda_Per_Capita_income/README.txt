Canada Per Capita Income Predictor
Overview

This project uses a Linear Regression model from scikit-learn to predict Canada's per capita income based on the year. The model is trained on historical per capita income data and generates predictions for future years.

Dataset

The training dataset contains two columns:

year – The year of the observation.
per_capita_income (US$) – Canada's per capita income in U.S. dollars.
Technologies Used
Python
Pandas
NumPy
scikit-learn (Linear Regression)
How It Works
Load the historical dataset.
Train a Linear Regression model using the year as the input feature.
Load a second CSV file containing years to predict.
Generate predicted per capita income values.
Save the results to a new CSV file named prediction_per_capita_income.csv.
Input

Example input CSV:

year
2020
2021
2022
Output

The program creates a new file named prediction_per_capita_income.csv containing:

year	per capita income (US$)
2020	Predicted Value
2021	Predicted Value
2022	Predicted Value
Purpose

This project demonstrates how to build, train, and use a simple machine learning regression model to make predictions using historical data.
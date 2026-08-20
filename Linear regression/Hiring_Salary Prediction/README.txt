# Hiring Salary Prediction Using Linear Regression

## Overview

This project demonstrates how to build a multiple linear regression model using Python and Scikit-learn to predict an employee's salary based on three features:

* Years of experience
* Test score
* Interview score

The goal is to understand the complete machine learning workflow, including data preprocessing, feature preparation, model training, and prediction.

## Dataset

The dataset contains the following columns:

* **Experience** – Years of work experience (stored as words such as "one", "two", "three")
* **Test Score (out of 10)** – Candidate's written test score
* **Interview Score (out of 10)** – Candidate's interview performance
* **Salary ($)** – Target value the model learns to predict

## Data Preprocessing

Before training the model, the dataset required several preprocessing steps:

### 1. Converting experience from words to numbers

The experience column was stored as text (for example, "one", "five", and "ten"). Since linear regression requires numerical inputs, these values were converted into integers.

### 2. Handling missing experience values

Missing values in the experience column were assumed to represent candidates with no prior experience. These missing values were replaced with **0** before training the model.

### 3. Handling missing test scores

Some candidates were missing test scores. Instead of removing those rows, the missing values were filled using the **median** test score. Using the median helps reduce the influence of unusually high or low scores.

## Exploratory Data Analysis

Scatter plots were created to explore the relationship between the input features and salary. These visualizations provided a general understanding of the data before training the model.

Because the model uses multiple input variables simultaneously, the scatter plots serve only as an initial visualization. The learned coefficients from the linear regression model provide a better indication of how strongly each feature contributes to the salary prediction.

## Model Training

A multiple linear regression model was trained using:

* Experience
* Test Score
* Interview Score

to predict:

* Salary

After fitting the model, the learned coefficients and intercept were examined to understand how each feature influences the predicted salary.

## Results

The model learned a linear equation relating the three input features to salary. Among the features, **experience received the largest coefficient**, indicating it had the strongest influence on salary predictions for this dataset.

The trained model can be used to estimate the salary of new candidates by providing their experience, test score, and interview score.

## Skills Demonstrated

* Data cleaning
* Handling missing values
* Feature engineering
* Data preprocessing
* Exploratory Data Analysis (EDA)
* Multiple Linear Regression
* Model interpretation
* Machine Learning with Scikit-learn

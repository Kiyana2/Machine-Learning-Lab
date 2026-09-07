# Student Productivity Prediction API

## Overview

This project uses a multiple linear regression model to predict student productivity based on several student-related factors.

The machine learning model was trained separately and then deployed as a REST API using FastAPI and Render. This allows other applications to send student information to the API and receive a predicted productivity score.

## Machine Learning Model

The model uses the following features:

- Gender
- Study hours per day
- Sleep hours
- Phone usage hours
- Attendance percentage
- Stress level
- Focus score

The target variable is:

- Productivity score

The trained model is saved as a `.pkl` file and loaded by the FastAPI application.

## API

The API provides a `/predict` endpoint that accepts the required student information and returns a predicted productivity score.

### Live API

[Student Productivity Prediction API](https://student-productivity-prediction-api.onrender.com)

### API Documentation

[Swagger UI](https://student-productivity-prediction-api.onrender.com/docs)

## API Usage

The `Student_Productivity_API_Demo.ipynb` notebook demonstrates how another Python application can send data to the deployed API and use the returned prediction.

Example:

```python
import requests

data = {
    "gender": 1,
    "study_hours_per_day": 5,
    "sleep_hours": 8,
    "phone_usage_hours": 10,
    "attendance_percentage": 100,
    "stress_level": 8,
    "focus_score": 6
}

response = requests.get(
    "https://student-productivity-prediction-api.onrender.com/predict",
    params=data
)

print(response.json())
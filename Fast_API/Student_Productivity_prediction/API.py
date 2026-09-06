from fastapi import FastAPI
import joblib

app = FastAPI()

model = joblib.load("student_productivity_prediction.pkl")


@app.get("/predict")
def predict(
    gender: float,
    study_hours_per_day: float,
    sleep_hours: float,
    phone_usage_hours: float,
    attendance_percentage: float,
    stress_level: float,
    focus_score: float
):
    prediction = model.predict([[
        gender,
        study_hours_per_day,
        sleep_hours,
        phone_usage_hours,
        attendance_percentage,
        stress_level,
        focus_score
    ]])

    return {
        "Student productivity prediction": prediction[0]
    }
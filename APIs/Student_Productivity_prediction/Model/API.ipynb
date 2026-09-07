{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "3536b2ed-c75d-44bb-ae58-8910511078c3",
   "metadata": {},
   "source": [
    "## Load model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "fc23ca6e-3bd6-4aac-97ce-40d438c4250d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting fastapi\n",
      "  Downloading fastapi-0.141.1-py3-none-any.whl.metadata (27 kB)\n",
      "Requirement already satisfied: starlette>=0.46.0 in C:\\Users\\tkiya\\anaconda3\\Lib\\site-packages (from fastapi) (1.3.1)\n",
      "Requirement already satisfied: pydantic>=2.9.0 in C:\\Users\\tkiya\\anaconda3\\Lib\\site-packages (from fastapi) (2.13.4)\n",
      "Requirement already satisfied: typing-extensions>=4.8.0 in C:\\Users\\tkiya\\anaconda3\\Lib\\site-packages (from fastapi) (4.16.0)\n",
      "Requirement already satisfied: typing-inspection>=0.4.2 in C:\\Users\\tkiya\\anaconda3\\Lib\\site-packages (from fastapi) (0.4.2)\n",
      "Requirement already satisfied: annotated-doc>=0.0.2 in C:\\Users\\tkiya\\anaconda3\\Lib\\site-packages (from fastapi) (0.0.4)\n",
      "Requirement already satisfied: annotated-types>=0.6.0 in C:\\Users\\tkiya\\anaconda3\\Lib\\site-packages (from pydantic>=2.9.0->fastapi) (0.7.0)\n",
      "Requirement already satisfied: pydantic-core==2.46.4 in C:\\Users\\tkiya\\anaconda3\\Lib\\site-packages (from pydantic>=2.9.0->fastapi) (2.46.4)\n",
      "Requirement already satisfied: anyio<5,>=3.6.2 in C:\\Users\\tkiya\\anaconda3\\Lib\\site-packages (from starlette>=0.46.0->fastapi) (4.12.1)\n",
      "Requirement already satisfied: idna>=2.8 in C:\\Users\\tkiya\\anaconda3\\Lib\\site-packages (from anyio<5,>=3.6.2->starlette>=0.46.0->fastapi) (3.18)\n",
      "Downloading fastapi-0.141.1-py3-none-any.whl (131 kB)\n",
      "Installing collected packages: fastapi\n",
      "Successfully installed fastapi-0.141.1\n"
     ]
    }
   ],
   "source": [
    "!pip install fastapi"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "cce635a6-336e-4318-a4e6-011533d3b058",
   "metadata": {},
   "outputs": [],
   "source": [
    "import joblib\n",
    "from fastapi import FastAPI\n",
    "app = FastAPI()\n",
    "model = joblib.load(\"student_productivity_prediction.pkl\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "f46d6cc6-685f-4175-8350-9eda4a8aa32d",
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.get(\"/predict\")\n",
    "def predict(gender: float, study_hours_per_day: float, sleep_hours: float, phone_usage_hours: float, attendance_percentage: float, stress_level: float, focus_score: float):\n",
    "    prediction = model.predict([[gender, study_hours_per_day, sleep_hours, phone_usage_hours, attendance_percentage, stress_level, focus_score]])\n",
    "\n",
    "    return {\"Student productivity prediction\": prediction[0]}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "97140455-4cdb-4110-a95d-f2d883b0b485",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.14.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

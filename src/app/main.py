from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()

model = joblib.load("app/target/model.pkl")

def preprocess_data(data):
    df = pd.DataFrame([data])

    # Data preprocessing as performed during training goes here

    return df

@app.post("/predict")
def predict(data: dict):
    processed_data = preprocess_data(data)
    prediction = model.predict(processed_data)
    return {"prediction": int(prediction[0])}

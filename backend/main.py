from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import os
import numpy as np

print("📂 Backend: Loading Model...")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Robust path finding
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "flashguard_model.pkl")

try:
    with open(MODEL_PATH, "rb") as f:
        ai_model = pickle.load(f)
    print("✅ Backend: Model Loaded Successfully!")
except Exception as e:
    print(f"❌ Backend: FAILED TO LOAD MODEL: {e}")

class TransactionData(BaseModel):
    amount: float
    oldbalanceOrg: float
    newbalanceOrig: float
    oldbalanceDest: float
    newbalanceDest: float
    location: str = "India"

@app.post("/predict")
def predict(data: TransactionData):
    # --- REALISM SCALE ---
    # We divide the real-world amounts by 10,000 so that 
    # ₹50,000 becomes 5.0 (which your model likes).
    scale_factor = 10000 
    
    scaled_features = np.array([[
        data.amount / scale_factor, 
        data.oldbalanceOrg / scale_factor, 
        data.newbalanceOrig / scale_factor, 
        data.oldbalanceDest / scale_factor, 
        data.newbalanceDest / scale_factor
    ]])

    # 🤖 PURE ML PREDICTION
    prediction = ai_model.predict(scaled_features)[0]
    
    status = "SUCCESS" if prediction == 1 else "BLOCKED"
    
    print(f"📥 Real Amount: ₹{data.amount} | Scaled: {data.amount/scale_factor} | Result: {status}")

    return {
        "status": status,
        "prediction": int(prediction),
        "amount": data.amount
    }

@app.get("/")
def health_check():
    return {"status": "Backend is ALIVE"}
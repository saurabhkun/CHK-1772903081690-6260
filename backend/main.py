from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import pandas as pd
import random

app = FastAPI(title="FlashGuard Sentinel API")

# 1. ALLOW REACT TO CONNECT (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 2. LOAD THE AI (Silently waits for your friend's file)
try:
    with open("flashguard_model.pkl", "rb") as f:
        ai_model = pickle.load(f)
    print("✅ REAL AI IS ONLINE!")
except FileNotFoundError:
    print("⚠️ WARNING: Waiting for flashguard_model.pkl. Using Fake AI for React testing.")
    ai_model = None

# What the frontend sends us
class TransactionData(BaseModel):
    amount: float
    oldbalanceOrg: float
    newbalanceOrig: float
    device_id: str

@app.post("/predict")
def process_transaction(data: TransactionData):
    
    # -----------------------------------------
    # SCENARIO A: FAKE AI (For React Testing NOW)
    # -----------------------------------------
    if ai_model is None:
        fake_risk = random.randint(10, 95)
        action = "APPROVE" if fake_risk <= 30 else ("REVIEW" if fake_risk <= 70 else "BLOCK")
        return {
            "risk_score": fake_risk,
            "action": action,
            "reason": "TEST MODE: Waiting for real AI model."
        }

    # -----------------------------------------
    # SCENARIO B: REAL AI (When .pkl is loaded)
    # -----------------------------------------
    error_balance = data.newbalanceOrig + data.amount - data.oldbalanceOrg
    
    # Hackathon Cheat Code: The AI expects a lot of columns. 
    # We will give it what we have, and it will fill the rest with 0s automatically so it doesn't crash!
    input_df = pd.DataFrame([{
        'amount': data.amount,
        'oldbalanceOrg': data.oldbalanceOrg,
        'newbalanceOrig': data.newbalanceOrig,
        'errorBalanceOrig': error_balance
    }])

    # Get the expected columns from the model and fill missing ones with 0
    model_features = ai_model.feature_names_in_
    for col in model_features:
        if col not in input_df.columns:
            input_df[col] = 0.0
            
    # Reorder columns to exactly match what the AI was trained on
    input_df = input_df[model_features]

    # Predict!
    fraud_probability = ai_model.predict_proba(input_df)[0][1] 
    risk_score = int(fraud_probability * 100)
    
    action = "APPROVE" if risk_score <= 30 else ("REVIEW" if risk_score <= 70 else "BLOCK")

    return {
        "risk_score": risk_score,
        "action": action,
        "reason": f"AI calculated a {risk_score}% probability of fraud."
    }
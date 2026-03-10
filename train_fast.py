import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

print("1. Loading your clean data...")
# Loading the file you successfully engineered earlier
df = pd.read_csv(r'data/processed_paysim.csv')

print("2. Prepping the AI target...")
y = df['isFraud']
X = df.drop(columns=['isFraud', 'isFlaggedFraud', 'step'])

print("3. Training the AI (Using your CPU to the max)...")
# n_jobs=-1 tells it to use every core of your i5 processor
model = RandomForestClassifier(n_estimators=50, max_depth=10, random_state=42, n_jobs=-1)
model.fit(X, y)

print("4. Saving the AI Brain...")
with open('backend/flashguard_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ DONE! flashguard_model.pkl is now in your backend folder!")
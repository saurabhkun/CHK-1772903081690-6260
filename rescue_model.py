import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle
import os

print("1. Loading your clean data...")
# Loading the file you successfully engineered earlier
df = pd.read_csv(r'data/processed_paysim.csv')

print("2. Prepping the AI target...")
y = df['isFraud']
X = df.drop(columns=['isFraud', 'isFlaggedFraud', 'step'])

print("3. Training the AI (Using your CPU to the max)...")
# n_jobs=-1 tells it to use every core of your processor
model = RandomForestClassifier(n_estimators=50, max_depth=10, random_state=42, n_jobs=-1)
model.fit(X, y)

print("4. Saving the AI Brain...")
# Ensure it goes straight to the backend folder
save_path = os.path.join('backend', 'flashguard_model.pkl')
with open(save_path, 'wb') as f:
    pickle.dump(model, f)

print(f"✅ DONE! {save_path} has been created. The AI is ready!")
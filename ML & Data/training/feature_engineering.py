import pandas as pd

def engineer_features(filepath):
    print("1. Loading raw transaction logs...")
    df = pd.read_csv(filepath, nrows=50000) # Only 50k for fast currenttesting
    
    print("2. Building Threat Indicators...")
    # I 1: Balance manipulation. 
    df['errorBalanceOrig'] = df['newbalanceOrig'] + df['amount'] - df['oldbalanceOrg']
    
    #  2 Converting transaction 'type' (text) into numbers (1s and 0s)
    df = pd.get_dummies(df, columns=['type'], drop_first=True)

    print("3. Cleaning up text data...")
    
    df = df.drop(columns=['nameOrig', 'nameDest'])
    
    print("4. Saving pure numeric data for the AI...")
   
    df.to_csv('data/processed_paysim.csv', index=False)
    print("✅ Feature engineering complete!")

if __name__ == "__main__":
    
    engineer_features(r"D:\FlashGuard\CHK-1772903081690-6260\data\paysim.csv")
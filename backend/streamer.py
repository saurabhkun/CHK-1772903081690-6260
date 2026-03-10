import requests
import time
import random

# Direct IP to avoid latency
URL = "http://127.0.0.1:8000/predict"

print("🚀 FlashGuard Live Simulation: STARTED")
print(f"📡 Feeding real-time transaction stream to: {URL}")
print("-" * 50)

while True:
    # 1. Generate realistic transaction amounts
    # Mix of low-value (Success) and high-value (Potential Block)
    amt = random.choice([450.0, 1200.0, 3500.0, 52000.0, 89000.0, 150.0])
    
    # 2. Dynamic Balance Logic (Looks better than static numbers)
    starting_balance = random.uniform(100000.0, 500000.0) 
    new_balance = starting_balance - amt
    
    dest_old = random.uniform(1000.0, 5000.0)
    dest_new = dest_old + amt

    sample_data = {
        "amount": round(amt, 2),
        "oldbalanceOrg": round(starting_balance, 2),
        "newbalanceOrig": round(new_balance, 2),
        "oldbalanceDest": round(dest_old, 2),
        "newbalanceDest": round(dest_new, 2),
        "location": random.choice(["Mumbai", "Delhi", "Bangalore", "Kolkata", "Remote IP"])
    }

    try:
        # 5-second timeout to prevent freezing
        response = requests.post(URL, json=sample_data, timeout=5)
        
        if response.status_code == 200:
            result = response.json()
            status = result.get('status')
            
            # 🎨 Color-coded console output for the demo
            icon = "✅" if status == "SUCCESS" else "🚨"
            print(f"{icon} TX: ₹{amt:<8} | Status: {status:<8} | Loc: {sample_data['location']}")
        else:
            print(f"⚠️ Server Error: {response.status_code}")
            
    except requests.exceptions.ConnectionError:
        print("❌ Connection Error: Backend is offline.")
    except Exception as e:
        print(f"❓ Error: {e}")

    # Faster stream for more "action" on the dashboard
    time.sleep(1.5)

# 🛡️ FlashGuard Pro: Real-Time Fraud Detection System
### *Advanced Behavioral Monitoring & ML-Powered Security*

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![Tailwind](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)

FlashGuard Pro is an end-to-end financial surveillance stack that uses Machine Learning to identify fraudulent transactions in real-time. It features a high-performance FastAPI backend, a persistent SQLite data store, and a dynamic React dashboard for live monitoring.



## 🚀 Key Features
* **Real-time ML Inference**: Processes transactions and returns risk scores in milliseconds.
* **Live Analytics Dashboard**: Visualizes transaction volume, spending patterns, and system health.
* **Persistent Storage**: Uses SQLite to maintain transaction history across sessions.
* **Automated Data Streamer**: Simulates a live bank feed using historical CSV data for demonstration.

---

## 🛠️ Tech Stack
* **Frontend**: React.js, Vite, Tailwind CSS, Recharts
* **Backend**: FastAPI (Python), Uvicorn
* **Database**: SQLite
* **Data Science**: Pandas, Scikit-learn (ML models)

---

## 🏁 Getting Started (Launch Sequence)

To see the live system in action, follow these steps in **four separate terminals**.

### 1️⃣ Terminal: The Backend Engine
```bash
cd backend
pip install -r requirements.txt
python main.py

```

*Initializes `flashguard.db` and listens on `http://127.0.0.1:8000`.*

### 2️⃣ Terminal: The Live Streamer

```bash
cd backend
python streamer.py

```

*Replays historical transaction data into the API to populate charts.*

### 3️⃣ Terminal: The Analytics Dashboard

```bash
cd frontend
npm install
npm run dev

```

*Visualizes real-time metrics and risk trends.*

### 4️⃣ Terminal: The Main FraudGuard App

```bash
cd fraudguard
npm install
npm run dev

```

*Launches the primary management interface.*

---

## 📊 Dashboard Overview

* **Transaction Volume**: Displays the throughput of the network in real-time.
* **Spending by Type**: Breaks down financial activity by category (Transfer, Payment, etc.).
* **System Health Radar**: A multi-dimensional view of Risk, Volume, Trust, and Diversity.

---

## ⚙️ Configuration

* **CSV Path**: The streamer looks for data in `data/processed_paysim.csv`.
* **API URL**: Configured to `http://127.0.0.1:8000` by default.
* **CORS**: Enabled for all origins (`*`) for easy local development.

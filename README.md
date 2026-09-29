# 🛡️ FraudShield AI

## Credit Card Fraud Detection using Machine Learning

FraudShield AI is a machine-learning based web application for detecting potentially fraudulent credit-card transactions.

The project uses a **Random Forest Classifier** trained on the Credit Card Fraud Detection dataset and provides a **Streamlit web interface** for:

- 🔍 Single transaction prediction
- 📂 Batch CSV prediction
- 📊 Fraud probability
- 🚨 Fraud / legitimate classification
- 🧪 Model information and preprocessing details

---

## 🚀 Project Architecture

```text
Transaction Data
       ↓
Preprocessing
       ↓
Amount & Time Scaling
       ↓
30 Model Features
       ↓
Random Forest
       ↓
Fraud Probability
       ↓
Fraud / Legitimate
       ↓
Streamlit Frontend
```

### Model Features

The deployed model uses 30 features:

```text
V1, V2, V3, ... V28
scaled_amount
scaled_time
```

The application automatically converts the user's:

- `Amount` → `scaled_amount`
- `Time` → `scaled_time`

so the user does not need to calculate scaled values manually.

---

## 📁 Project Structure

```text
FraudShield-AI/
│
├── app.py
├── fraud_detection_model.pkl
├── requirements.txt
├── README.md
└── .gitignore
```

### Files

| File | Purpose |
|---|---|
| `app.py` | Streamlit frontend and prediction logic |
| `fraud_detection_model.pkl` | Trained Random Forest model + preprocessing objects |
| `requirements.txt` | Python dependencies |
| `README.md` | Project documentation |
| `.gitignore` | Files that should not be uploaded to GitHub |

> `creditcard.csv` is not required to run the deployed application. It was used for model training. Do not upload the full dataset to GitHub unless you have a specific reason and have checked its size/licensing.

---

# 💻 Run the Project Locally

## 1. Install Python

Install Python from the official Python website:

https://www.python.org/downloads/

Python 3.13 is a good choice for this project.

Check the installation:

```bash
python --version
```

On some macOS/Linux systems, use:

```bash
python3 --version
```

---

# 🪟 Windows

### Step 1 — Download the project

You can either:

### Option A — Download ZIP

On GitHub:

```text
Code → Download ZIP
```

Extract the ZIP file.

GitHub officially supports downloading a repository as a ZIP snapshot. 

### Option B — Clone using Git

```powershell
git clone https://github.com/YOUR_USERNAME/FraudShield-AI.git
```

Then:

```powershell
cd FraudShield-AI
```

---

### Step 2 — Create a virtual environment

```powershell
python -m venv venv
```

Activate it:

```powershell
venv\Scripts\activate
```

You should see:

```text
(venv)
```

at the beginning of your terminal.

---

### Step 3 — Install dependencies

```powershell
python -m pip install -r requirements.txt
```

---

### Step 4 — Run the application

```powershell
python -m streamlit run app.py
```

The browser should open:

```text
http://localhost:8501
```

If it does not open automatically, copy that address into your browser.

---

# 🍎 macOS

### Step 1 — Download or clone the project

Clone:

```bash
git clone https://github.com/YOUR_USERNAME/FraudShield-AI.git
```

Enter the folder:

```bash
cd FraudShield-AI
```

Or download the ZIP from GitHub and extract it.

---

### Step 2 — Create virtual environment

```bash
python3 -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

---

### Step 3 — Install dependencies

```bash
python3 -m pip install -r requirements.txt
```

---

### Step 4 — Run

```bash
python3 -m streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

# 🐧 Linux

### Step 1 — Download or clone

```bash
git clone https://github.com/YOUR_USERNAME/FraudShield-AI.git
```

```bash
cd FraudShield-AI
```

---

### Step 2 — Create virtual environment

```bash
python3 -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

---

### Step 3 — Install dependencies

```bash
python3 -m pip install -r requirements.txt
```

---

### Step 4 — Run

```bash
python3 -m streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

# 📦 Required Python Packages

The `requirements.txt` file contains:

```text
streamlit
pandas
numpy
scikit-learn
joblib
```

Install everything with:

```bash
python -m pip install -r requirements.txt
```

or on macOS/Linux:

```bash
python3 -m pip install -r requirements.txt
```

---

# 🔍 How to Use the Application

## 1. Dashboard

The dashboard displays:

- Model name
- Number of features
- Classification threshold
- Application status
- ML pipeline

---

## 2. Single Transaction

Go to:

```text
🔍 Single Transaction
```

Enter:

```text
Transaction Time
Transaction Amount
V1
V2
V3
...
V28
```

You do **not** need to enter:

```text
scaled_amount
scaled_time
```

The application calculates them automatically.

Click:

```text
🚀 Analyze Transaction
```

The model returns:

```text
Fraud Probability
Classification
```

Possible classifications:

```text
✅ LEGITIMATE
```

or

```text
🚨 FRAUD
```

---

## 3. Batch Prediction

Go to:

```text
📂 Batch Prediction
```

Upload a CSV containing:

```text
Time
V1
V2
...
V28
Amount
```

The application automatically:

1. Loads the CSV
2. Scales `Amount`
3. Scales `Time`
4. Creates the 30 model features
5. Runs the Random Forest model
6. Calculates fraud probability
7. Generates predictions

The results can be downloaded as:

```text
fraud_predictions.csv
```

---

# 🧠 Machine Learning Model

The project evaluates multiple approaches including:

- Logistic Regression
- Random Forest
- XGBoost
- Isolation Forest
- Autoencoder

The deployed prototype uses **Random Forest**.

### Random Forest Results

| Metric | Result |
|---|---:|
| Accuracy | 99.93% |
| Precision | 81.25% |
| Recall | 79.59% |
| F1 Score | 80.41% |
| ROC-AUC | 89.78% |

Because the dataset is highly imbalanced, precision, recall and F1-score are important metrics alongside accuracy.

---

# 📊 Dataset

The project was trained using the Credit Card Fraud Detection dataset containing anonymized transaction features.

The dataset contains:

- `Time`
- `V1`–`V28`
- `Amount`
- `Class`

`Class` represents the target:

```text
0 = Legitimate
1 = Fraud
```

The dataset was used during training and is **not required to run the Streamlit application**.

---

# ⚠️ Important Note

The `V1`–`V28` features are anonymized numerical features from the dataset. They are not normal human-readable banking fields.

Therefore, the single-transaction interface is mainly intended as a **machine-learning project demonstration**.

This project is an academic/prototype fraud-detection system and should not be treated as a production banking fraud system.

---

# 🌐 Deploying the Application

The project can be deployed using Streamlit Community Cloud.

Basic process:

```text
GitHub Repository
       ↓
Streamlit Community Cloud
       ↓
Select Repository
       ↓
Select app.py
       ↓
Deploy
       ↓
Public Web Application
```

Make sure the GitHub repository contains:

```text
app.py
fraud_detection_model.pkl
requirements.txt
README.md
```

---

# 🛠️ Troubleshooting

## `streamlit is not recognized`

Instead of:

```bash
streamlit run app.py
```

use:

```bash
python -m streamlit run app.py
```

On macOS/Linux:

```bash
python3 -m streamlit run app.py
```

---

## `ModuleNotFoundError`

Run:

```bash
python -m pip install -r requirements.txt
```

or:

```bash
python3 -m pip install -r requirements.txt
```

---

## Model cannot be loaded

Make sure this file is in the same directory as `app.py`:

```text
fraud_detection_model.pkl
```

Correct:

```text
FraudShield-AI/
├── app.py
├── fraud_detection_model.pkl
└── requirements.txt
```

Incorrect:

```text
FraudShield-AI/
├── app.py
└── models/
    └── fraud_detection_model.pkl
```

unless `app.py` is updated to use that path.

---

# 👨‍💻 Author

**Anurag Bhadra**

B.Tech Computer Science Engineering

---

## ⭐ Project

<img width="1919" height="865" alt="image" src="https://github.com/user-attachments/assets/d6e890ec-e766-4a2b-9b2e-a68ae59afd49" />
<img width="1919" height="864" alt="image" src="https://github.com/user-attachments/assets/70db932b-f2e0-4853-8aae-944c3775a4e9" />



If you find this project useful, consider giving the GitHub repository a star.

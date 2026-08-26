# 🛡️ AI RiskGuard – Intelligent Fraud Detection System

### Predicting Transaction Risk with Machine Learning

![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-Machine%20Learning-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)
![Random Forest](https://img.shields.io/badge/Model-Random%20Forest-4CAF50?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

---

## 📌 Project Overview

**AI RiskGuard** is a Machine Learning-powered fraud risk assessment system designed to analyze transaction-related information and estimate the probability of fraudulent activity.

The application uses a trained **Random Forest Classifier** to evaluate transaction patterns and generate:

- 📊 Fraud Probability
- 🎯 Risk Score out of 100
- 🚦 Risk Classification
- 🤖 AI-Based Recommendation

Transactions are categorized into three risk levels:

🟢 **Low Risk**  
🟡 **Medium Risk**  
🔴 **High Risk**

The project combines a Machine Learning pipeline with an interactive **Streamlit dashboard**, allowing users to enter transaction details and receive an understandable fraud risk assessment.

---

## ❓ Why This Project Matters

Digital transactions generate large volumes of data, making manual fraud assessment difficult to scale.

AI RiskGuard explores how **supervised Machine Learning** can be applied to a real-world-inspired fraud detection problem by analyzing behavioral and security-related transaction features.

This project demonstrates:

- Practical application of classification algorithms
- Feature-based fraud risk analysis
- Machine Learning model training and evaluation
- Model interpretability using feature importance
- Converting model predictions into understandable risk insights
- Building an interactive Machine Learning application with Streamlit

> **Note:** The project uses synthetically generated transaction data for educational and portfolio purposes.

---

# ✨ Key Features

### 🔍 Fraud Risk Prediction

Users can enter transaction details and receive a Machine Learning-based fraud assessment.

### 📊 Fraud Probability

The Random Forest model estimates the probability that a transaction may be fraudulent.

### 🎯 Risk Score

Fraud probability is converted into a simple **Risk Score from 0 to 100**.

### 🚦 Three-Level Risk Classification

Transactions are classified as:

- 🟢 Low Risk
- 🟡 Medium Risk
- 🔴 High Risk

### 🤖 AI Risk Recommendation

The application provides a human-readable recommendation based on the calculated risk level.

### 📈 Model Performance Analytics

The dashboard displays important Machine Learning evaluation metrics:

- Accuracy
- Precision
- Recall
- F1 Score

### 🧩 Model Insights

The application includes:

- Confusion Matrix
- Feature Importance Visualization

### 🎨 Interactive Dashboard

A professional dark-themed Streamlit interface organizes the project into multiple sections, including:

- AI Risk Assessment
- Model Performance Analytics
- Model Insights
- About AI RiskGuard
- Fraud Risk Prediction

---

# 🔄 System Workflow

```text
User Transaction Input
        │
        ▼
Feature Preparation
        │
        ▼
Random Forest Classifier
        │
        ▼
Fraud Probability Prediction
        │
        ▼
Risk Score Calculation
        │
        ▼
Risk Classification
Low / Medium / High
        │
        ▼
AI Recommendation
        │
        ▼
Result Displayed on Streamlit Dashboard
```

---

# 🧠 Machine Learning Approach

AI RiskGuard uses a **supervised binary classification approach**.

During training, transaction records are labeled as either:

- `0` → Legitimate Transaction
- `1` → Fraudulent Transaction

The model learns relationships between transaction features and fraud patterns.

For a new transaction, the trained model calculates:

```text
Probability of Fraud
        ↓
Risk Score (0–100)
        ↓
Risk Classification
        ↓
Recommendation
```

The project uses:

## 🌳 Random Forest Classifier

A **Random Forest Classifier** was used because it is well suited for structured tabular data and provides useful feature importance information.

Advantages include:

- Handles multiple numerical and binary input features
- Combines predictions from multiple decision trees
- Helps reduce overfitting compared to a single decision tree
- Provides feature importance scores
- Works effectively with structured transaction data

---

# 📋 Input Features

The Machine Learning model analyzes the following transaction-related features:

| # | Feature | Description |
|---|---|---|
| 1 | Transaction Amount | Monetary value of the transaction |
| 2 | Transaction Hour | Hour at which the transaction occurs |
| 3 | Transactions in Last 24 Hours | Number of transactions performed within the last 24 hours |
| 4 | Account Age (Days) | Age of the user account |
| 5 | Failed Login Attempts | Number of failed login attempts |
| 6 | International Transaction | Whether the transaction is international |
| 7 | Trusted Device | Whether the transaction is performed using a trusted device |

---

# 🚦 Risk Classification System

The predicted fraud probability is converted into a risk score.

| Risk Score | Classification | Recommendation |
|---|---|---|
| 0–29 | 🟢 **Low Risk** | Transaction appears relatively safe |
| 30–59 | 🟡 **Medium Risk** | Transaction should be reviewed carefully |
| 60–100 | 🔴 **High Risk** | Manual verification is recommended |

---

# 📊 Model Performance

The Random Forest model was evaluated using a train-test split.

| Metric | Score |
|---|---:|
| 🎯 Accuracy | **64.8%** |
| 🔎 Precision | **37.1%** |
| 📡 Recall | **64.2%** |
| ⚖️ F1 Score | **47.0%** |

These metrics provide different perspectives on the model's classification performance:

- **Accuracy** measures overall prediction correctness.
- **Precision** measures how reliable fraud predictions are.
- **Recall** measures how effectively fraudulent transactions are identified.
- **F1 Score** provides a balance between precision and recall.

---

# 📈 Model Insights & Visualizations

AI RiskGuard includes visual analysis of the trained model.

## 🧩 Confusion Matrix

The confusion matrix helps visualize:

- Correct legitimate predictions
- Correct fraud predictions
- False positives
- False negatives

This provides a clearer understanding of how the model performs across both classes.

## 📊 Feature Importance

Random Forest feature importance is used to understand which transaction features have the strongest influence on the model.

The project generates a feature importance chart automatically during model training.

This improves the interpretability of the Machine Learning model and helps demonstrate how different transaction characteristics contribute to fraud risk estimation.

---

# 🛠️ Technology Stack

| Category | Technology |
|---|---|
| Programming Language | Python |
| Web Application Framework | Streamlit |
| Machine Learning | Scikit-learn |
| ML Model | Random Forest Classifier |
| Data Processing | Pandas |
| Numerical Computing | NumPy |
| Model Saving | Joblib |
| Visualization | Matplotlib |

---

# 📂 Project Structure

```text
AI-RiskGuard/
│
├── app.py
├── train_model.py
├── requirements.txt
├── README.md
│
├── data/
│   └── transactions.csv
│
└── models/
    ├── riskguard_model.pkl
    ├── metrics.json
    ├── confusion_matrix.png
    └── feature_importance.png
```

### File Description

| File / Folder | Purpose |
|---|---|
| `app.py` | Main Streamlit application |
| `train_model.py` | Generates synthetic data and trains the Random Forest model |
| `requirements.txt` | Required Python dependencies |
| `data/transactions.csv` | Generated transaction dataset |
| `models/riskguard_model.pkl` | Trained Machine Learning model |
| `models/metrics.json` | Saved model evaluation metrics |
| `models/confusion_matrix.png` | Confusion matrix visualization |
| `models/feature_importance.png` | Feature importance visualization |

---

# ⚙️ Installation

## 1️⃣ Clone the Repository

```bash
git clone <YOUR_REPOSITORY_URL>
```

Move into the project directory:

```bash
cd AI-RiskGuard
```

---

## 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Train the Model

If the model files are not already available, run:

```bash
python train_model.py
```

This will generate:

- Synthetic transaction data
- Trained Random Forest model
- Model evaluation metrics
- Confusion Matrix
- Feature Importance chart

---

## 5️⃣ Run the Application

```bash
streamlit run app.py
```

The Streamlit application will open in your browser.

---

# 🖥️ How to Use AI RiskGuard

### Step 1

Launch the Streamlit application.

### Step 2

Navigate to the **Fraud Risk Prediction** section.

### Step 3

Enter transaction information:

- Transaction Amount
- Transaction Hour
- Transactions in Last 24 Hours
- Account Age
- Failed Login Attempts
- International Transaction
- Trusted Device

### Step 4

Click:

```text
Analyze Transaction
```

### Step 5

The system generates:

- Fraud Probability
- Risk Score
- Risk Classification
- AI Recommendation

---

# 🧪 Example Prediction Results

The application was tested using different transaction scenarios.

## 🟢 Low Risk Example

Example transaction characteristics:

- Lower transaction amount
- Normal transaction frequency
- Older account
- No failed login attempts
- Domestic transaction
- Trusted device

### Result

| Output | Value |
|---|---|
| Fraud Probability | **25.56%** |
| Risk Score | **25.6 / 100** |
| Classification | 🟢 **LOW RISK** |
| Recommendation | Transaction appears relatively safe |

---

## 🔴 High Risk Example

Example transaction characteristics:

- High transaction amount
- High transaction frequency
- New account
- Multiple failed login attempts
- International transaction
- Untrusted device

### Result

| Output | Value |
|---|---|
| Fraud Probability | **74.19%** |
| Risk Score | **74.2 / 100** |
| Classification | 🔴 **HIGH RISK** |
| Recommendation | Manual verification is strongly recommended |

---

# 📸 Application Screenshots

Add your project screenshots inside a `screenshots` folder.

Suggested screenshots:

### 🖥️ Main Dashboard

```text
screenshots/dashboard.png
```

### 🟢 Low Risk Prediction

```text
screenshots/low-risk.png
```

### 🔴 High Risk Prediction

```text
screenshots/high-risk.png
```

### 📊 Model Performance

```text
screenshots/model-performance.png
```

### 📈 Model Insights

```text
screenshots/model-insights.png
```

After adding screenshots, you can display them like this:

```markdown
![AI RiskGuard Dashboard](screenshots/dashboard.png)
```

---

# 🎓 Key Learning Outcomes

Through building AI RiskGuard, the following concepts and skills were applied:

- Supervised Machine Learning
- Binary Classification
- Random Forest Classifier
- Train-Test Split
- Model Evaluation
- Accuracy, Precision, Recall, and F1 Score
- Confusion Matrix Analysis
- Feature Importance
- Synthetic Dataset Generation
- Data Handling with Pandas
- Model Serialization using Joblib
- Interactive Application Development using Streamlit
- Translating ML predictions into understandable risk assessments

---

# 🚀 Future Improvements

Possible future improvements include:

- 📊 Training with a larger real-world fraud dataset
- 🤖 Comparing additional Machine Learning algorithms
- 📈 Hyperparameter tuning to improve model performance
- 🗄️ Database integration for transaction history
- 🔐 User authentication
- 📉 Handling class imbalance using advanced techniques
- 🌐 Deploying the application online
- 📊 Adding more advanced fraud analytics and monitoring

---

# ⚠️ Disclaimer

AI RiskGuard is an **educational and portfolio Machine Learning project**.

The current version uses **synthetically generated transaction data** and is intended to demonstrate Machine Learning concepts, model evaluation, and interactive application development.

This project does not use:

- Real banking data
- Real-time financial transactions
- Production fraud detection infrastructure
- Production-grade security systems

Predictions generated by this application should **not be used as real financial or security decisions**.

---

# 🏁 Conclusion

**AI RiskGuard** demonstrates how Machine Learning can be applied to a practical fraud detection problem by transforming transaction-related data into meaningful risk assessments.

The project covers an end-to-end Machine Learning workflow:

```text
Synthetic Data Generation
        ↓
Data Preparation
        ↓
Random Forest Model Training
        ↓
Model Evaluation
        ↓
Model Saving
        ↓
Interactive Streamlit Application
        ↓
Fraud Risk Prediction
        ↓
Risk Assessment & Recommendation
```

By combining **Machine Learning, model evaluation, feature importance analysis, and an interactive user interface**, AI RiskGuard demonstrates practical experience in building an end-to-end ML application.

The project serves as a strong foundation for further work in:

- Machine Learning
- Fraud Analytics
- Risk Assessment
- Data Science
- Intelligent Decision Support Systems

---

## 👤 Author

**Akshaya B**

CSE (AI & ML) Student  
Aspiring Machine Learning Engineer

GitHub: Add your GitHub profile link here  
LinkedIn: Add your LinkedIn profile link here

---

⭐ **If you found this project interesting, consider giving the repository a star!**

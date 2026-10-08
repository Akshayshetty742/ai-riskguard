import streamlit as st
import pandas as pd
import joblib
import json
import os
model = joblib.load("models/riskguard_model.pkl")
st.set_page_config(
    page_title="AI RiskGuard",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
.stApp { background-color: #0E1117; color: #E6EAF0; }
.block-container { max-width: 1400px; padding-top: 2rem; padding-bottom: 3rem; }

.hero {
    background: linear-gradient(135deg, #111827, #1E293B);
    padding: 2rem 2.5rem;
    border-radius: 20px;
    border: 1px solid #2D3A4F;
    margin-bottom: 2rem;
}
.brand { font-size: 2.6rem; font-weight: 800; color: white; }
.brand span { color: #60A5FA; }
.tagline { color: #94A3B8; font-size: 1.05rem; margin-top: 0.5rem; }

.section-title {
    font-size: 1.7rem; font-weight: 700; color: #F8FAFC;
    margin-top: 1.5rem; margin-bottom: 0.5rem;
}
.input-card {
    background-color: #161D29; border: 1px solid #2D3A4F;
    border-radius: 18px; padding: 1.2rem 1.5rem; margin-bottom: 1rem;
}
.card-title { font-size: 1.45rem; font-weight: 700; color: white; }

.risk-banner {
    background: #161D29; border-radius: 16px; padding: 1.5rem 1.8rem;
    margin: 1rem 0 1.5rem 0; border: 1px solid #334155;
}
.risk-title { font-size: 1.5rem; font-weight: 800; color: white; }
.risk-description { margin-top: 0.5rem; color: #CBD5E1; font-size: 1rem; }

.metric-card {
    background: #161D29; border: 1px solid #2D3A4F;
    border-radius: 16px; padding: 1.4rem; min-height: 145px; text-align: center;
}
.metric-label { color: #94A3B8; font-size: 0.95rem; margin-bottom: 0.7rem; }
.metric-value { color: #F8FAFC; font-size: 2rem; font-weight: 800; }
.metric-subtitle { color: #64748B; font-size: 0.8rem; margin-top: 0.5rem; }

.analysis-card {
    background: #161D29; border: 1px solid #2D3A4F;
    border-radius: 16px; padding: 1.2rem 1.5rem; margin-top: 1rem;
}
.analysis-card h3 { margin: 0; color: white; }
.analysis-card p { color: #94A3B8; margin-bottom: 0; }

.recommendation-card {
    background: rgba(37, 99, 235, 0.12);
    border: 1px solid rgba(96, 165, 250, 0.4);
    border-radius: 16px; padding: 1.4rem 1.6rem;
}
.recommendation-card h3 { color: #93C5FD; margin-top: 0; }
.recommendation-card p { color: #E2E8F0; margin-bottom: 0; }

.risk-factor-card {
    background: #1B202B;
    border: 1px solid #3B4454;
    border-left: 4px solid #F59E0B;
    border-radius: 12px;
    padding: 1rem 1.2rem;
    margin-bottom: 0.8rem;
    color: #F8FAFC;
}
.safe-card {
    background: rgba(34, 197, 94, 0.12);
    border: 1px solid rgba(34, 197, 94, 0.4);
    border-left: 4px solid #22C55E;
    border-radius: 14px;
    padding: 1.2rem 1.4rem;
    color: #BBF7D0;
}
.performance-card {
    background: #161D29;
    border: 1px solid #2D3A4F;
    border-radius: 16px;
    padding: 1.3rem;
    text-align: center;
}
.performance-label {
    color: #94A3B8;
    font-size: 0.9rem;
    margin-bottom: 0.5rem;
}
.performance-value {
    color: #60A5FA;
    font-size: 1.8rem;
    font-weight: 800;
}
.chart-card {
    background: #161D29;
    border: 1px solid #2D3A4F;
    border-radius: 16px;
    padding: 1.2rem;
    min-height: 100%;
}
.chart-title {
    color: #F8FAFC;
    font-size: 1.15rem;
    font-weight: 700;
    margin-bottom: 1rem;
}
.system-card {
    background: linear-gradient(135deg, #172033, #111827);
    border: 1px solid #2D4C73;
    border-radius: 16px;
    padding: 1.4rem 1.6rem;
    margin-top: 1rem;
}
.system-card h3 {
    margin-top: 0;
    color: #93C5FD;
}
.system-card p {
    margin-bottom: 0;
    color: #CBD5E1;
}
div.stButton > button {
    height: 3.2rem; border-radius: 12px; font-size: 1rem; font-weight: 700;
}
.footer {
    text-align: center; color: #64748B; margin-top: 3rem;
    padding-top: 1rem; font-size: 0.9rem;
}

.insight-card {
    background: #1c2636;
    border: 1px solid #30435f;
    border-radius: 15px;
    padding: 25px;
    min-height: 190px;
    margin-bottom: 25px;
}

.insight-card h3 {
    color: #8ab4f8;
    margin-bottom: 15px;
}

.insight-card p {
    color: #aeb9c9;
    font-size: 15px;
    line-height: 1.6;
}

.insight-value {
    color: #7db5ff;
    font-size: 32px;
    font-weight: bold;
    margin-top: 20px;
}

.about-card {
    background: #192536;
    border: 1px solid #30435f;
    border-radius: 18px;
    padding: 30px;
    margin-top: 15px;
}

.about-card h2 {
    color: #8ab4f8;
}

.about-card p {
    color: #b8c2d1;
    line-height: 1.7;
}

.about-grid {
    display: flex;
    gap: 20px;
    margin-top: 25px;
}

.about-grid > div {
    flex: 1;
    background: #222d3e;
    border-radius: 12px;
    padding: 20px;
}

.about-grid h3 {
    color: #d5e5ff;
}

.footer {
    text-align: center;
    margin-top: 50px;
    padding: 25px;
    border-top: 1px solid #29384e;
    color: #7f8da3;
}

/* ============================================================
   ABOUT AI RISKGUARD
============================================================ */

.about-container {
    margin-top: 20px;
}

.about-header {
    background: #1e293b;
    border: 1px solid #334155;
    border-radius: 16px;
    padding: 30px;
    margin-bottom: 25px;
}

.about-header h2 {
    color: #9ec5ff;
    font-size: 32px;
    margin-bottom: 12px;
}

.about-header p {
    color: #cbd5e1;
    font-size: 17px;
    line-height: 1.7;
}

.about-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
    margin-bottom: 30px;
}

.about-card {
    background: #1e293b;
    border: 1px solid #334155;
    border-radius: 16px;
    padding: 25px;
    min-height: 220px;
    transition: 0.3s;
}

.about-card:hover {
    transform: translateY(-5px);
    border-color: #60a5fa;
}

.about-icon {
    font-size: 32px;
    margin-bottom: 15px;
}

.about-card h3 {
    color: #f1f5f9;
    font-size: 22px;
    margin-bottom: 12px;
}

.about-card p {
    color: #94a3b8;
    font-size: 16px;
    line-height: 1.6;
}

.technology-section {
    background: #1e293b;
    border: 1px solid #334155;
    border-radius: 16px;
    padding: 28px;
}

.technology-section h3 {
    color: #f1f5f9;
    font-size: 25px;
    margin-bottom: 20px;
}

.tech-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 15px;
}

.tech-card {
    background: #24364a;
    border: 1px solid #36506b;
    border-radius: 10px;
    padding: 18px;
    text-align: center;
    color: #93c5fd;
    font-size: 16px;
    font-weight: 600;
}

.tech-card:hover {
    background: #2b4159;
}


</style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_model():
    return joblib.load("models/riskguard_model.pkl")

try:
    model = load_model()
except FileNotFoundError:
    st.error("❌ Model file not found. Please run train_model.py first.")
    st.stop()
except Exception as e:
    st.error(f"❌ Error loading model: {e}")
    st.stop()

st.markdown("""
<div class="hero">
    <div class="brand">🛡️ AI <span>RiskGuard</span></div>
    <div class="tagline">
        AI-Powered Payment Fraud Detection & Risk Intelligence Platform
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="section-title">🔍 Transaction Risk Assessment</div>',
    unsafe_allow_html=True
)
st.write(
    "Enter transaction information below and let the Machine Learning "
    "model analyze potential fraud risk."
)

input_col1, input_col2 = st.columns(2)

with input_col1:
    st.markdown("""
    <div class="input-card">
        <div class="card-title">💳 Transaction Details</div>
    </div>
    """, unsafe_allow_html=True)

    transaction_amount = st.number_input(
        "Transaction Amount (₹)", min_value=1.0, value=2000.0
    )
    transaction_hour = st.slider(
        "Transaction Hour", min_value=0, max_value=23, value=12
    )
    transactions_last_24h = st.number_input(
        "Transactions in Last 24 Hours", min_value=0, value=2
    )
    account_age_days = st.number_input(
        "Account Age (Days)", min_value=1, value=365
    )

with input_col2:
    st.markdown("""
    <div class="input-card">
        <div class="card-title">🔐 Security Information</div>
    </div>
    """, unsafe_allow_html=True)

    failed_attempts = st.number_input(
        "Failed Login Attempts", min_value=0, value=0
    )
    is_international = st.selectbox(
        "International Transaction?", ["No", "Yes"]
    )
    device_trusted = st.selectbox(
        "Trusted Device?", ["Yes", "No"]
    )

international_value = 1 if is_international == "Yes" else 0
trusted_device_value = 1 if device_trusted == "Yes" else 0

st.write("")
analyze_button = st.button(
    "🔍 Analyze Transaction Risk",
    use_container_width=True
)

if analyze_button:
    input_data = pd.DataFrame([{
        "transaction_amount": transaction_amount,
        "transaction_hour": transaction_hour,
        "transactions_last_24h": transactions_last_24h,
        "account_age_days": account_age_days,
        "failed_attempts": failed_attempts,
        "is_international": international_value,
        "device_trusted": trusted_device_value
    }])

    fraud_probability = model.predict_proba(input_data)[0][1]
    risk_score = fraud_probability * 100

    if risk_score < 30:
        risk_level = "LOW RISK"
        risk_icon = "🟢"
        risk_color = "#22C55E"
        recommendation = (
            "The transaction appears relatively safe. "
            "No immediate security action is required."
        )
    elif risk_score < 60:
        risk_level = "MEDIUM RISK"
        risk_icon = "🟡"
        risk_color = "#F59E0B"
        recommendation = (
            "The transaction shows moderate risk indicators. "
            "Review is recommended before approval."
        )
    else:
        risk_level = "HIGH RISK"
        risk_icon = "🔴"
        risk_color = "#EF4444"
        recommendation = (
            "Potential fraudulent activity detected. "
            "Manual verification is strongly recommended."
        )

    risk_factors = []

    if transaction_amount > 8000:
        risk_factors.append("High transaction amount detected")
    if transactions_last_24h > 8:
        risk_factors.append("Unusually high transaction frequency")
    if failed_attempts > 3:
        risk_factors.append("Multiple failed login attempts")
    if international_value == 1:
        risk_factors.append("International transaction detected")
    if trusted_device_value == 0:
        risk_factors.append("Transaction initiated from an untrusted device")
    if account_age_days < 30:
        risk_factors.append("New account with limited transaction history")

    st.divider()
    st.markdown(
        '<div class="section-title">🤖 AI Risk Assessment</div>',
        unsafe_allow_html=True
    )

    st.markdown(f"""
    <div class="risk-banner" style="border-left: 6px solid {risk_color};">
        <div class="risk-title">{risk_icon} {risk_level}</div>
        <div class="risk-description">{recommendation}</div>
    </div>
    """, unsafe_allow_html=True)

    metric1, metric2, metric3 = st.columns(3)

    with metric1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Fraud Probability</div>
            <div class="metric-value">{fraud_probability * 100:.2f}%</div>
            <div class="metric-subtitle">Predicted fraud likelihood</div>
        </div>
        """, unsafe_allow_html=True)

    with metric2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Risk Score</div>
            <div class="metric-value">{risk_score:.1f}/100</div>
            <div class="metric-subtitle">Overall transaction risk</div>
        </div>
        """, unsafe_allow_html=True)

    with metric3:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Risk Classification</div>
            <div class="metric-value" style="font-size:1.5rem;">{risk_level}</div>
            <div class="metric-subtitle">AI-generated classification</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="analysis-card">
        <h3>📊 Risk Score Analysis</h3>
        <p>The score represents the estimated probability that this transaction may be fraudulent.</p>
    </div>
    """, unsafe_allow_html=True)

    st.progress(min(100, max(0, int(risk_score))))
    st.caption(
        "🟢 0–29 = Low Risk    |    "
        "🟡 30–59 = Medium Risk    |    "
        "🔴 60–100 = High Risk"
    )

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"""
    <div class="recommendation-card">
        <h3>🤖 AI Recommendation</h3>
        <p>{recommendation}</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">⚠️ Detected Risk Factors</div>',
        unsafe_allow_html=True
    )

    if risk_factors:
        factor_col1, factor_col2 = st.columns(2)

        for index, factor in enumerate(risk_factors):
            target = factor_col1 if index % 2 == 0 else factor_col2
            with target:
                st.markdown(
                    f'<div class="risk-factor-card">⚠️ {factor}</div>',
                    unsafe_allow_html=True
                )
    else:
        st.markdown("""
        <div class="safe-card">
            ✅ No major risk factors detected.
            The transaction currently appears safe based on the information provided.
        </div>
        """, unsafe_allow_html=True)

st.divider()
st.markdown(
    '<div class="section-title">📊 Model Performance Analytics</div>',
    unsafe_allow_html=True
)
st.write(
    "Performance metrics generated during Machine Learning model training."
)

metrics_path = "models/metrics.json"

if os.path.exists(metrics_path):
    try:
        with open(metrics_path, "r") as file:
            metrics = json.load(file)

        perf1, perf2, perf3, perf4 = st.columns(4)

        performance_items = [
            ("🎯 Accuracy", metrics.get("accuracy", 0), "Overall prediction correctness"),
            ("🔎 Precision", metrics.get("precision", 0), "Fraud prediction reliability"),
            ("📡 Recall", metrics.get("recall", 0), "Fraud detection coverage"),
            ("⚖️ F1 Score", metrics.get("f1_score", 0), "Balanced model performance"),
        ]

        for column, item in zip(
            [perf1, perf2, perf3, perf4], performance_items
        ):
            label, value, subtitle = item
            with column:
                st.markdown(f"""
                <div class="performance-card">
                    <div class="performance-label">{label}</div>
                    <div class="performance-value">{value * 100:.1f}%</div>
                    <div class="metric-subtitle">{subtitle}</div>
                </div>
                """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(
            '<div class="section-title">📈 Model Insights</div>',
            unsafe_allow_html=True
        )

        chart_col1, chart_col2 = st.columns(2)

        with chart_col1:
            st.markdown("""
            <div class="chart-card">
                <div class="chart-title">🧩 Confusion Matrix</div>
            </div>
            """, unsafe_allow_html=True)
            if os.path.exists("models/confusion_matrix.png"):
                st.image(
                    "models/confusion_matrix.png",
                    use_container_width=True
                )
            else:
                st.info("Confusion matrix image not found.")

        with chart_col2:
            st.markdown("""
            <div class="chart-card">
                <div class="chart-title">📊 Feature Importance</div>
            </div>
            """, unsafe_allow_html=True)
            if os.path.exists("models/feature_importance.png"):
                st.image(
                    "models/feature_importance.png",
                    use_container_width=True
                )
            else:
                st.info("Feature importance chart not found.")

        st.markdown("""
        <div class="system-card">
            <h3>🧠 AI RiskGuard Intelligence</h3>
            <p>
                The model evaluates transaction behaviour, account history,
                login activity, international activity and device trust to
                estimate potential fraud risk.
            </p>
        </div>
        """, unsafe_allow_html=True)

    except Exception as e:
        st.error(f"Error loading model performance data: {e}")

else:
    st.warning(
        "⚠️ Model performance data not found. "
        "Please run train_model.py first."
    )

st.markdown("""
<div class="footer">
    🛡️ AI RiskGuard &nbsp; | &nbsp;
    Machine Learning Powered Fraud Detection System
    <br><br>
    Built with Python, Streamlit and Scikit-learn
</div>
""", unsafe_allow_html=True)


# =========================================================
# MODEL PERFORMANCE SUMMARY
# =========================================================

st.markdown(
    """
    <div class="section-title">
        📊 Model Performance Summary
    </div>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
        <div class="insight-card">
            <h3>🎯 Accuracy</h3>
            <p>
                Accuracy shows how often the model correctly classifies
                transactions as legitimate or fraudulent.
            </p>
            <div class="insight-value">
                {:.1f}%
            </div>
        </div>
        """.format(metrics["accuracy"] * 100),
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div class="insight-card">
            <h3>🔎 Fraud Detection</h3>
            <p>
                The model successfully identifies fraudulent transactions
                based on transaction behaviour and security information.
            </p>
            <div class="insight-value">
                {:.1f}%
            </div>
        </div>
        """.format(metrics["recall"] * 100),
        unsafe_allow_html=True
    )


st.markdown(
    """
    <div class="ai-recommendation">
        <h2>🧠 AI RiskGuard Intelligence</h2>
        <p>
            The machine learning model analyzes transaction amount,
            transaction frequency, account age, failed login attempts,
            international activity and device trust to identify
            potentially fraudulent transactions.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# ============================================================
# ABOUT AI RISKGUARD
# ============================================================

st.markdown(
"""
<div class="section-title">
ℹ️ About AI RiskGuard
</div>

<div class="about-container">

<div class="about-header">
<h2>AI-Powered Fraud Detection System</h2>

<p>
AI RiskGuard is a Machine Learning based payment fraud detection
system developed using Python, Streamlit and Random Forest.
</p>
</div>

<div class="about-grid">

<div class="about-card">

<div class="about-icon">ML</div>

<h3>Machine Learning</h3>

<p>
Uses a Random Forest Classifier to analyze transaction behaviour
and identify possible fraud.
</p>

</div>


<div class="about-card">

<div class="about-icon">SEC</div>

<h3>Security Analysis</h3>

<p>
Considers failed login attempts, international transactions
and device trust information.
</p>

</div>


<div class="about-card">

<div class="about-icon">DATA</div>

<h3>Data Insights</h3>

<p>
Displays model performance, confusion matrix and feature
importance for better understanding.
</p>

</div>

</div>


<div class="technology-section">

<h3>Technology Used</h3>

<div class="tech-grid">

<div class="tech-card">Python</div>

<div class="tech-card">Streamlit</div>

<div class="tech-card">Scikit-learn</div>

<div class="tech-card">Random Forest</div>

</div>

</div>

</div>
""",
unsafe_allow_html=True
)

st.markdown("---")

st.header("Fraud Risk Prediction")

st.write(
    "Enter the transaction details below and let the AI RiskGuard model analyze the fraud risk."
)

col1, col2 = st.columns(2)

with col1:

    transaction_amount = st.number_input(
        "Transaction Amount",
        min_value=0.0,
        value=1000.0,
        step=100.0,
        key="prediction_transaction_amount"
    )

    transaction_hour = st.number_input(
        "Transaction Hour (0-23)",
        min_value=0,
        max_value=23,
        value=12,
        key="prediction_transaction_hour"
    )

    transactions_last_24h = st.number_input(
        "Transactions in Last 24 Hours",
        min_value=0,
        value=1,
        key="prediction_transactions_24h"
    )

    account_age_days = st.number_input(
        "Account Age (Days)",
        min_value=1,
        value=365,
        key="prediction_account_age"
    )


with col2:

    failed_attempts = st.number_input(
        "Failed Login Attempts",
        min_value=0,
        value=0,
        key="prediction_failed_attempts"
    )

    international_option = st.selectbox(
        "International Transaction?",
        ["No", "Yes"],
        key="prediction_international"
    )

    device_option = st.selectbox(
        "Is Device Trusted?",
        ["Yes", "No"],
        key="prediction_device_trusted"
    )


if st.button(
    "Analyze Transaction",
    use_container_width=True,
    key="prediction_analyze_button"
):

    is_international = (
        1 if international_option == "Yes" else 0
    )

    device_trusted = (
        1 if device_option == "Yes" else 0
    )

    input_data = pd.DataFrame(
        [[
            transaction_amount,
            transaction_hour,
            transactions_last_24h,
            account_age_days,
            failed_attempts,
            is_international,
            device_trusted
        ]],
        columns=[
            "transaction_amount",
            "transaction_hour",
            "transactions_last_24h",
            "account_age_days",
            "failed_attempts",
            "is_international",
            "device_trusted"
        ]
    )

    prediction = model.predict(input_data)[0]

    probability = (
        model.predict_proba(input_data)[0][1] * 100
    )

    st.markdown("---")

    if prediction == 1:

        st.error("Potential Fraud Detected!")

        st.metric(
            "Fraud Probability",
            f"{probability:.2f}%"
        )

        st.warning(
            "This transaction has been identified as potentially fraudulent."
        )

    else:

        st.success(
            "Transaction Appears Legitimate"
        )

        st.metric(
            "Fraud Probability",
            f"{probability:.2f}%"
        )

        st.info(
            "The model considers this transaction to have a lower fraud risk."
        )
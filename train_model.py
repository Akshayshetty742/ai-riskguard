import pandas as pd
import numpy as np
import joblib
import json
import os
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    precision_score,
    recall_score,
    f1_score,
    ConfusionMatrixDisplay
)

# =========================================================
# CREATE REQUIRED FOLDERS
# =========================================================

os.makedirs("models", exist_ok=True)
os.makedirs("data", exist_ok=True)


# =========================================================
# SET RANDOM SEED
# =========================================================

np.random.seed(42)


# =========================================================
# GENERATE SYNTHETIC TRANSACTION DATA
# =========================================================

n_samples = 5000

data = pd.DataFrame({
    "transaction_amount": np.random.exponential(
        scale=2000,
        size=n_samples
    ),

    "transaction_hour": np.random.randint(
        0,
        24,
        n_samples
    ),

    "transactions_last_24h": np.random.poisson(
        3,
        n_samples
    ),

    "account_age_days": np.random.randint(
        1,
        2000,
        n_samples
    ),

    "failed_attempts": np.random.poisson(
        1,
        n_samples
    ),

    "is_international": np.random.randint(
        0,
        2,
        n_samples
    ),

    "device_trusted": np.random.randint(
        0,
        2,
        n_samples
    )
})


# =========================================================
# CREATE FRAUD PATTERNS
# =========================================================

fraud_probability = (
    0.03
    + 0.35 * (data["transaction_amount"] > 8000)
    + 0.25 * (data["transactions_last_24h"] > 8)
    + 0.35 * (data["failed_attempts"] > 3)
    + 0.15 * (data["is_international"] == 1)
    + 0.25 * (data["device_trusted"] == 0)
    + 0.30 * (data["account_age_days"] < 30)
)

fraud_probability = np.clip(
    fraud_probability,
    0,
    0.95
)


# =========================================================
# CREATE FRAUD LABEL
# =========================================================

data["is_fraud"] = np.random.binomial(
    1,
    fraud_probability
)


# =========================================================
# SAVE DATASET
# =========================================================

data.to_csv(
    "data/transactions.csv",
    index=False
)


# =========================================================
# FEATURES AND TARGET
# =========================================================

X = data.drop(
    "is_fraud",
    axis=1
)

y = data["is_fraud"]


# =========================================================
# TRAIN / TEST SPLIT
# =========================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# =========================================================
# TRAIN RANDOM FOREST MODEL
# =========================================================

model = RandomForestClassifier(
    n_estimators=300,
    max_depth=12,
    min_samples_split=5,
    random_state=42,
    class_weight="balanced"
)

model.fit(
    X_train,
    y_train
)


# =========================================================
# PREDICTIONS
# =========================================================

y_pred = model.predict(X_test)


# =========================================================
# CALCULATE METRICS
# =========================================================

precision = precision_score(
    y_test,
    y_pred
)

recall = recall_score(
    y_test,
    y_pred
)

f1 = f1_score(
    y_test,
    y_pred
)

accuracy = model.score(
    X_test,
    y_test
)


# =========================================================
# PRINT RESULTS
# =========================================================

print("\n===== AI RISKGUARD MODEL RESULTS =====")

print(f"Accuracy:  {accuracy:.2f}")
print(f"Precision: {precision:.2f}")
print(f"Recall:    {recall:.2f}")
print(f"F1 Score:  {f1:.2f}")

print("\nClassification Report:")

print(
    classification_report(
        y_test,
        y_pred
    )
)


# =========================================================
# CONFUSION MATRIX
# =========================================================

cm = confusion_matrix(
    y_test,
    y_pred
)

print("Confusion Matrix:")
print(cm)


# =========================================================
# SAVE TRAINED MODEL
# =========================================================

joblib.dump(
    model,
    "models/riskguard_model.pkl"
)


# =========================================================
# SAVE METRICS
# =========================================================

metrics = {
    "accuracy": float(accuracy),
    "precision": float(precision),
    "recall": float(recall),
    "f1_score": float(f1)
}

with open(
    "models/metrics.json",
    "w"
) as file:

    json.dump(
        metrics,
        file,
        indent=4
    )


# =========================================================
# DARK THEME COLORS
# =========================================================

BACKGROUND_COLOR = "#111827"
CARD_COLOR = "#1f2937"
TEXT_COLOR = "#e5e7eb"
GRID_COLOR = "#374151"
ACCENT_COLOR = "#60a5fa"


# =========================================================
# CREATE DARK CONFUSION MATRIX
# =========================================================

fig, ax = plt.subplots(
    figsize=(7, 5)
)

fig.patch.set_facecolor(
    BACKGROUND_COLOR
)

ax.set_facecolor(
    CARD_COLOR
)

display = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=[
        "Normal",
        "Fraud"
    ]
)

display.plot(
    ax=ax,
    cmap="Blues",
    colorbar=True
)

ax.set_title(
    "AI RiskGuard - Confusion Matrix",
    color=TEXT_COLOR,
    fontsize=16,
    fontweight="bold",
    pad=15
)

ax.set_xlabel(
    "Predicted Transaction",
    color=TEXT_COLOR
)

ax.set_ylabel(
    "Actual Transaction",
    color=TEXT_COLOR
)

ax.tick_params(
    colors=TEXT_COLOR
)

for text in ax.texts:
    text.set_color(
        TEXT_COLOR
    )

plt.tight_layout()

plt.savefig(
    "models/confusion_matrix.png",
    dpi=150,
    bbox_inches="tight",
    facecolor=BACKGROUND_COLOR
)

plt.close()


# =========================================================
# FEATURE IMPORTANCE
# =========================================================

importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)


# =========================================================
# CLEAN FEATURE NAMES
# =========================================================

feature_names = {
    "transaction_amount": "Transaction Amount",
    "transaction_hour": "Transaction Hour",
    "transactions_last_24h": "Transactions (24h)",
    "account_age_days": "Account Age",
    "failed_attempts": "Failed Attempts",
    "is_international": "International Transaction",
    "device_trusted": "Trusted Device"
}

importance["Feature"] = importance["Feature"].map(
    feature_names
)


# =========================================================
# CREATE DARK FEATURE IMPORTANCE CHART
# =========================================================

fig, ax = plt.subplots(
    figsize=(9, 5)
)

fig.patch.set_facecolor(
    BACKGROUND_COLOR
)

ax.set_facecolor(
    CARD_COLOR
)

ax.barh(
    importance["Feature"],
    importance["Importance"],
    color=ACCENT_COLOR
)

ax.set_xlabel(
    "Importance Score",
    color=TEXT_COLOR
)

ax.set_title(
    "AI RiskGuard - Feature Importance",
    color=TEXT_COLOR,
    fontsize=16,
    fontweight="bold",
    pad=15
)

ax.tick_params(
    colors=TEXT_COLOR
)

ax.invert_yaxis()

ax.grid(
    axis="x",
    linestyle="--",
    alpha=0.2,
    color=GRID_COLOR
)

for spine in ax.spines.values():
    spine.set_color(
        GRID_COLOR
    )

plt.tight_layout()

plt.savefig(
    "models/feature_importance.png",
    dpi=150,
    bbox_inches="tight",
    facecolor=BACKGROUND_COLOR
)

plt.close()


# =========================================================
# SUCCESS MESSAGE
# =========================================================

print("\n========================================")
print("AI RISKGUARD MODEL TRAINING COMPLETE!")
print("========================================")

print("Model saved successfully!")
print("Metrics saved to models/metrics.json")
print("Confusion matrix saved successfully!")
print("Feature importance chart saved successfully!")
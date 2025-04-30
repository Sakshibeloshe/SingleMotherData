# SingleMotherData

# 💼 Finance Toolkit for Single Mothers

This was created as a trial for a hackathon. Our problem statement was for finace managing for single mothers. The apps name would have been **MOMentum**.
This folder contains two Python-based desktop apps designed to support single mothers in managing finances and estimating monthly savings. The tools are built with **Tkinter** and basic machine learning integration (for prediction).

---

## 📁 Contents

### 1. `finance_manager.py`

An all-in-one financial guidance app for single mothers. It includes:
- 📊 Budget Allocation (Savings, Needs, Wants)
- 💼 Job Recommendations based on education & job status
- 🚨 Emergency Fund Calculator
- 📈 Investment Advice
- 🎓 Grants & Aid Suggestions

### 2. `savings_predictor.py`

A machine learning–powered tool that predicts potential monthly savings using:
- Income & Expenses
- Education & Job Status
- Debt
- Derived features (disposable income, debt-to-income ratio, etc.)

It uses:
- A pre-trained regression model (`budget_model.pkl`)
- Scaler (`scaler.pkl`)
- Label Encoders (`label_encoders.pkl`)

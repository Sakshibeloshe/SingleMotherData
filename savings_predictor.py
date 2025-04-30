import tkinter as tk
import numpy as np
import joblib

def predict_savings():
    try:
        # Load model and encoders
        model = joblib.load("budget_model.pkl")
        scaler = joblib.load("scaler.pkl")
        label_encoders = joblib.load("label_encoders.pkl")

        # Get user input
        income = float(entry_income.get())
        expenses = float(entry_expenses.get())
        education = education_var.get()
        job_status = job_status_var.get()
        debt = float(entry_debt.get())

        # Encode categorical values
        education_encoded = label_encoders['Education Level'].transform([education])[0]
        job_status_encoded = label_encoders['Job Status'].transform([job_status])[0]

        # Compute additional features
        disposable_income = income - expenses
        debt_to_income_ratio = debt / (income + 1)  # Avoid division by zero
        log_debt = np.log1p(debt)

        # Create input array
        user_data = np.array([[income, expenses, education_encoded, job_status_encoded, debt, disposable_income,
                               debt_to_income_ratio, log_debt]])
        user_data = scaler.transform(user_data)

        # Predict savings potential
        savings_potential = model.predict(user_data)[0]
        result_label.config(text=f"Predicted Savings Potential: {savings_potential:.2f}")
    except Exception as e:
        result_label.config(text=f"Error: {str(e)}")

# Create GUI window
root = tk.Tk()
root.title("Savings Potential Predictor")
root.geometry("400x400")

# Labels and entry fields
tk.Label(root, text="Monthly Income:").pack()
entry_income = tk.Entry(root)
entry_income.pack()

tk.Label(root, text="Monthly Expenses:").pack()
entry_expenses = tk.Entry(root)
entry_expenses.pack()

tk.Label(root, text="Education Level:").pack()
education_var = tk.StringVar()
education_var.set("High School")  # Default value
tk.OptionMenu(root, education_var, "High School", "Bachelor", "Master", "PhD").pack()

tk.Label(root, text="Job Status:").pack()
job_status_var = tk.StringVar()
job_status_var.set("Unemployed")  # Default value
tk.OptionMenu(root, job_status_var, "Unemployed", "Part-time", "Full-time", "Freelancer").pack()

tk.Label(root, text="Debt Amount:").pack()
entry_debt = tk.Entry(root)
entry_debt.pack()

# Predict button
tk.Button(root, text="Predict Monthly Savings Potential", command=predict_savings).pack()

# Label to display result
result_label = tk.Label(root, text="")
result_label.pack()

# Run the application
root.mainloop()

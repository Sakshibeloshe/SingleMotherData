import tkinter as tk
#added investment suggestions and grants/aid recommendations

class SingleMotherFinanceManager:
    def __init__(self, income, expenses, education, job_status, debt):
        self.income = income
        self.expenses = expenses
        self.education = education
        self.job_status = job_status
        self.debt = debt

    def budget_allocation(self):
        savings = self.income * 0.2  # 20% for savings
        needs = self.income * 0.5  # 50% for essential expenses
        wants = self.income * 0.3  # 30% for non-essential expenses
        return {"Savings": savings, "Needs": needs, "Wants": wants}

    def suggest_job_opportunities(self):
        jobs = {
            "No Education & No Job": ["Online Data Entry", "Retail Work", "Home-based Services"],
            "Educated but Unemployed": ["Freelancing", "Remote Customer Support", "Tutoring"],
            "Educated & Employed": ["Higher-Paying Jobs", "Side Hustles", "Investments"]
        }
        return jobs.get(self.education + " & " + self.job_status, ["Consult Career Coach"])

    def emergency_fund_suggestion(self):
        recommended_fund = self.expenses * 3  # 3 months of expenses as an emergency fund
        return recommended_fund if self.debt == 0 else recommended_fund * 1.5  # If debt exists, increase buffer

    def investment_suggestions(self):
        if self.income > 3000:
            return ["Index Funds", "High-Yield Savings Account", "Retirement Plans"]
        else:
            return ["Micro-investing Apps", "Emergency Fund First"]

    def grant_and_aid_suggestions(self):
        return ["Local Government Assistance", "Single Mother Scholarships", "Non-Profit Financial Aid"]

    def get_recommendations(self):
        budget = self.budget_allocation()
        jobs = self.suggest_job_opportunities()
        emergency_fund = self.emergency_fund_suggestion()
        investments = self.investment_suggestions()
        grants = self.grant_and_aid_suggestions()
        return budget, jobs, emergency_fund, investments, grants


# GUI Application
def calculate_finance():
    try:
        income = float(entry_income.get())
        expenses = float(entry_expenses.get())
        education = education_var.get()
        job_status = job_status_var.get()
        debt = float(entry_debt.get())

        finance_manager = SingleMotherFinanceManager(income, expenses, education, job_status, debt)
        budget, jobs, emergency_fund, investments, grants = finance_manager.get_recommendations()

        budget_text = "\n".join([f"{k}: ${v:.2f}" for k, v in budget.items()])
        jobs_text = "\n".join(jobs)
        investments_text = "\n".join(investments)
        grants_text = "\n".join(grants)

        result_label.config(
            text=f"Budget Allocation:\n{budget_text}\n\nJob Recommendations:\n{jobs_text}\n\nEmergency Fund: ${emergency_fund:.2f}\n\nInvestment Suggestions:\n{investments_text}\n\nAvailable Grants & Aid:\n{grants_text}")
    except Exception as e:
        result_label.config(text=f"Error: {str(e)}")


# Create GUI window
root = tk.Tk()
root.title("Finance Manager for Single Mothers")
root.geometry("400x600")

# Labels and entry fields
tk.Label(root, text="Monthly Income:").pack()
entry_income = tk.Entry(root)
entry_income.pack()

tk.Label(root, text="Monthly Expenses:").pack()
entry_expenses = tk.Entry(root)
entry_expenses.pack()

tk.Label(root, text="Education Level:").pack()
education_var = tk.StringVar()
education_var.set("No Education")  # Default value
tk.OptionMenu(root, education_var, "No Education", "Educated").pack()

tk.Label(root, text="Job Status:").pack()
job_status_var = tk.StringVar()
job_status_var.set("No Job")  # Default value
tk.OptionMenu(root, job_status_var, "No Job", "Unemployed", "Employed").pack()

tk.Label(root, text="Debt Amount:").pack()
entry_debt = tk.Entry(root)
entry_debt.pack()

# Calculate button
tk.Button(root, text="Calculate Finance", command=calculate_finance).pack()

# Label to display result
result_label = tk.Label(root, text="", justify="left")
result_label.pack()

# Run the application
root.mainloop()

import json
import os
from datetime import datetime


EXPENSE_DATA_FILE = "expense_data.json"
BUDGET_DATA_FILE = "budget_data.json"


if not os.path.exists(EXPENSE_DATA_FILE):
    with open(EXPENSE_DATA_FILE, "w") as f:
        json.dump({}, f)

if not os.path.exists(BUDGET_DATA_FILE):
    with open(BUDGET_DATA_FILE, "w") as f:
        json.dump({}, f)


def log_expense():
    print("\nLog Expense")
    with open(EXPENSE_DATA_FILE, "r") as f:
        expenses = json.load(f)

    expense_name = input("Enter expense name: ")
    amount = float(input("Enter expense amount: "))
    category = input("Enter expense category: ")
    date = datetime.now().strftime("%Y-%m-%d")

    if date not in expenses:
        expenses[date] = []

    expenses[date].append({"name": expense_name, "amount": amount, "category": category})

    with open(EXPENSE_DATA_FILE, "w") as f:
        json.dump(expenses, f)

    print("Expense logged successfully.")

def view_expenses():
    print("\nView Expenses")
    with open(EXPENSE_DATA_FILE, "r") as f:
        expenses = json.load(f)

    for date, entries in expenses.items():
        print("\nDate:", date)
        for entry in entries:
            print("  - Name:", entry["name"])
            print("    Amount:", entry["amount"])
            print("    Category:", entry["category"])

def set_budget():
    print("\nSet Budget")
    with open(BUDGET_DATA_FILE, "r") as f:
        budgets = json.load(f)

    category = input("Enter category to set budget for: ")
    budget_amount = float(input("Enter budget amount: "))

    budgets[category] = budget_amount

    with open(BUDGET_DATA_FILE, "w") as f:
        json.dump(budgets, f)

    print("Budget set successfully.")

def view_budgets():
    print("\nView Budgets")
    with open(BUDGET_DATA_FILE, "r") as f:
        budgets = json.load(f)

    for category, amount in budgets.items():
        print("Category:", category)
        print("Budget Amount:", amount)


def main():
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Log Expense")
        print("2. View Expenses")
        print("3. Set Budget")
        print("4. View Budgets")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            log_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            set_budget()
        elif choice == "4":
            view_budgets()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

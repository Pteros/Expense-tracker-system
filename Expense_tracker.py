import os
import json
import matplotlib.pyplot as plt
from datetime import datetime

# Define the file where expenses will be stored
EXPENSES_FILE = "expenses.json"

# Define the expense categories
DEFAULT_EXPENSE_CATEGORIES = ["Food", "Transportation", "Entertainment", "Other"]

class Expense:
    def __init__(self, date, amount, category, description):
        self.date = date
        self.amount = amount
        self.category = category
        self.description = description

def load_expenses():
    if os.path.exists(EXPENSES_FILE):
        with open(EXPENSES_FILE, "r") as file:
            return [Expense(**expense_data) for expense_data in json.load(file)]
    else:
        return []

def save_expenses(expenses):
    with open(EXPENSES_FILE, "w") as file:
        json.dump([expense.__dict__ for expense in expenses], file, indent=4)

def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def validate_amount(amount_str):
    try:
        float(amount_str)
        return True
    except ValueError:
        return False

def display_expenses(expenses):
    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. Date: {expense.date}, Amount: ${expense.amount:.2f}, Category: {expense.category}, Description: {expense.description}")

def main():
    expenses = load_expenses()
    categories = DEFAULT_EXPENSE_CATEGORIES

    while True:
        print("\nExpense Tracking System Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Generate Report")
        print("4. Sort Expenses")
        print("5. Filter Expenses")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            date = input("Enter expense date (YYYY-MM-DD): ")
            if not validate_date(date):
                print("Invalid date format. Please use YYYY-MM-DD.")
                continue

            amount = input("Enter expense amount: ")
            if not validate_amount(amount):
                print("Invalid amount format. Please enter a valid number.")
                continue

            print("Expense Categories:")
            for i, category in enumerate(categories, start=1):
                print(f"{i}. {category}")

            category_choice = int(input("Select expense category (or enter a new category): ")) - 1
            if category_choice < 0 or category_choice >= len(categories):
                new_category = input("Enter a new category: ")
                categories.append(new_category)
                category = new_category
            else:
                category = categories[category_choice]

            description = input("Enter expense description: ")

            new_expense = Expense(date, float(amount), category, description)
            expenses.append(new_expense)
            save_expenses(expenses)
            print("Expense added successfully!")

        elif choice == "2":
            display_expenses(expenses)

        elif choice == "3":
            total_expenses = sum(expense.amount for expense in expenses)
            print(f"Total Expenses: ${total_expenses:.2f}")

            category_expenses = {}
            for category in categories:
                category_expenses[category] = sum(expense.amount for expense in expenses if expense.category == category)

            for category, amount in category_expenses.items():
                print(f"{category} Expenses: ${amount:.2f}")

            # Visualization using Matplotlib
            plt.bar(category_expenses.keys(), category_expenses.values())
            plt.xlabel("Expense Categories")
            plt.ylabel("Amount ($)")
            plt.title("Expense Distribution by Category")
            plt.xticks(rotation=45)
            plt.show()

        elif choice == "4":
            sort_option = input("Sort by (date/amount/category): ").lower()
            if sort_option not in ["date", "amount", "category"]:
                print("Invalid sort option.")
                continue

            expenses.sort(key=lambda x: getattr(x, sort_option))
            display_expenses(expenses)

        elif choice == "5":
            filter_option = input("Filter by (date/category): ").lower()
            if filter_option not in ["date", "category"]:
                print("Invalid filter option.")
                continue

            filter_value = input(f"Enter {filter_option} to filter by: ")

            filtered_expenses = [expense for expense in expenses if getattr(expense, filter_option) == filter_value]
            display_expenses(filtered_expenses)

        elif choice == "6":
            print("Exiting Expense Tracking System. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

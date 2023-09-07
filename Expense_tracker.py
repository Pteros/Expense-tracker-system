import os
import csv
import datetime
import matplotlib.pyplot as plt

# Constants for menu options
MENU_OPTIONS = {
    1: "Add Expense",
    2: "View Expenses",
    3: "View Statistics",
    4: "Generate Report",
    5: "Exit",
}

# Constants for CSV file headers
CSV_HEADERS = ["Date", "Amount", "Category", "Description"]

# Function to load expenses from CSV
def load_expenses():
    expenses = []
    if os.path.exists("expenses.csv"):
        with open("expenses.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                expenses.append(row)
    return expenses

# Function to save expenses to CSV
def save_expenses(expenses):
    with open("expenses.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=CSV_HEADERS)
        writer.writeheader()
        writer.writerows(expenses)

# Function to add a new expense
def add_expense(expenses):
    while True:
        try:
            date_str = input("Enter the expense date (YYYY-MM-DD): ")
            date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            amount = float(input("Enter the expense amount: "))
            category = input("Enter the expense category: ")
            description = input("Enter a short description: ")
            expenses.append({"Date": date, "Amount": amount, "Category": category, "Description": description})
            save_expenses(expenses)
            print("Expense added successfully!")
            break
        except ValueError:
            print("Invalid input. Please enter a valid date and amount.")

# Function to view expenses
def view_expenses(expenses):
    # Implement sorting and filtering options here
    pass

# Function to view statistics
def view_statistics(expenses):
    # Calculate and display statistics like total expenses, average expenses by category, etc.
    pass

# Function to generate a report
def generate_report(expenses):
    # Generate and display a report with expense details
    pass

# Main function
def main():
    expenses = load_expenses()
    while True:
        print("\nExpense Tracking System Menu:")
        for key, value in MENU_OPTIONS.items():
            print(f"{key}. {value}")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            view_statistics(expenses)
        elif choice == "4":
            generate_report(expenses)
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
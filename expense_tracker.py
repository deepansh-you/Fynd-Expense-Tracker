import csv
from expense import Expense
from category import Category

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.categories = []
        self.load_from_csv()

    def add_expense(self, expense):
        self.expenses.append(expense)
        self.save_to_csv()

    def delete_expense(self, index):
        if 0 <= index < len(self.expenses):
            del self.expenses[index]
            self.save_to_csv()
            print(f"Deleted expense at index {index}")
        else:
            print("Invalid index")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
        for idx, expense in enumerate(self.expenses):
            print(f"{idx}: {expense}")

    def filter_by_category(self, category_name):
        filtered = [expense for expense in self.expenses if expense.category == category_name]
        if not filtered:
            print(f"No expenses found for category '{category_name}'")
        for expense in filtered:
            print(expense)

    def save_to_csv(self, filename='data/expenses.csv'):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Amount', 'Date', 'Category', 'Description'])
            for expense in self.expenses:
                writer.writerow([expense.amount, expense.date, expense.category, expense.description])

    def load_from_csv(self, filename='data/expenses.csv'):
        try:
            with open(filename, mode='r') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    if row:
                        amount, date, category, description = row
                        self.expenses.append(Expense(float(amount), date, category, description))
        except FileNotFoundError:
            print("No previous expenses found, starting fresh.")

    def add_category(self, category):
        self.categories.append(category)

    def list_categories(self):
        if not self.categories:
            print("No categories available.")
        else:
            for index, category in enumerate(self.categories):
                print(f"{index}: {category.name}")


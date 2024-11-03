from expense import Expense
from expense_tracker import ExpenseTracker
from category import Category

def display_menu():
    print("\nExpense Tracker Menu:")
    print("1. Add Category")
    print("2. Add Expense")
    print("3. View All Expenses")
    print("4. Delete Expense")
    print("5. Filter by Category")
    print("6. List Categories")
    print("0. Exit")
    print()

def add_expense(tracker):
    try:
        amount = float(input("Enter amount: "))
        date = input("Enter date (YYYY-MM-DD): ")
        tracker.list_categories()
        category_index = int(input("Select category index: "))
        if 0 <= category_index < len(tracker.categories):
            category = tracker.categories[category_index].name
        else:
            print("Invalid category index.")
            return
        description = input("Enter description (optional): ")
        expense = Expense(amount, date, category, description)
        tracker.add_expense(expense)
        print("Expense added successfully!")
    except ValueError as e:
        print(f"Error: {e}. Please enter valid inputs.")

def delete_expense(tracker):
    tracker.view_expenses()
    try:
        index = int(input("Enter the index of the expense to delete: "))
        tracker.delete_expense(index)
    except ValueError:
        print("Invalid input. Please enter a number.")

def filter_expenses_by_category(tracker):
    category_name = input("Enter category name to filter by: ")
    tracker.filter_by_category(category_name)

def add_category(tracker):
    name = input("Enter new category name: ")
    tracker.add_category(Category(name))
    print(f"Category '{name}' added successfully!")

def main():
    tracker = ExpenseTracker()

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            add_category(tracker)
        elif choice == '2':
            add_expense(tracker)
        elif choice == '3':
            tracker.view_expenses()
        elif choice == '4':
            delete_expense(tracker)
        elif choice == '5':
            filter_expenses_by_category(tracker)
        elif choice == '6':
            tracker.list_categories()
        elif choice == '0':
            print("Exiting the Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()

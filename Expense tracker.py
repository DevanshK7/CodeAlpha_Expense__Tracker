from tabulate import tabulate
from datetime import datetime

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.summary = {}

    def add_expense(self, date, category, amount):
        expense = {'date': date, 'category': category, 'amount': amount}
        self.expenses.append(expense)
        
        if category in self.summary:
            self.summary[category] += amount
        else:
            self.summary[category] = amount

    def display_expenses(self):
        if not self.expenses:
            print("No expenses to display.")
            return
        
        table = [[idx + 1, expense['date'], expense['category'], expense['amount']] for idx, expense in enumerate(self.expenses)]
        headers = ["Index", "Date", "Category", "Amount"]
        print(tabulate(table, headers, tablefmt="grid"))

    def display_summary(self):
        if not self.summary:
            print("No summary available.")
            return

        table = [[category, total] for category, total in self.summary.items()]
        headers = ["Category", "Total Amount"]
        print(tabulate(table, headers, tablefmt="grid"))

    def display_total_expenses(self):
        total = sum(expense['amount'] for expense in self.expenses)
        print(f"Total Expenses: ${total}")

    def delete_expense(self, index):
        if 0 <= index < len(self.expenses):
            expense = self.expenses.pop(index)
            self.summary[expense['category']] -= expense['amount']
            if self.summary[expense['category']] == 0:
                del self.summary[expense['category']]
            print("Expense deleted successfully.")
        else:
            print("Invalid index. Please try again.")

    def edit_expense(self, index, new_date, new_category, new_amount):
        if 0 <= index < len(self.expenses):
            old_expense = self.expenses[index]
            self.summary[old_expense['category']] -= old_expense['amount']
            if self.summary[old_expense['category']] == 0:
                del self.summary[old_expense['category']]
            
            self.expenses[index] = {'date': new_date, 'category': new_category, 'amount': new_amount}
            
            if new_category in self.summary:
                self.summary[new_category] += new_amount
            else:
                self.summary[new_category] = new_amount

            print("Expense edited successfully.")
        else:
            print("Invalid index. Please try again.")

def main():
    tracker = ExpenseTracker()
    
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. Display All Expenses")
        print("3. Display Summary by Category")
        print("4. Display Total Expenses")
        print("5. Delete Expense")
        print("6. Edit Expense")
        print("7. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            date = input("Enter expense date (YYYY-MM-DD): ")
            try:
                datetime.strptime(date, '%Y-%m-%d')
            except ValueError:
                print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
                continue

            category = input("Enter expense category: ")
            amount = float(input("Enter expense amount: "))
            tracker.add_expense(date, category, amount)
        elif choice == '2':
            tracker.display_expenses()
        elif choice == '3':
            tracker.display_summary()
        elif choice == '4':
            tracker.display_total_expenses()
        elif choice == '5':
            tracker.display_expenses()
            try:
                index = int(input("Enter the index of the expense to delete: ")) - 1
                tracker.delete_expense(index)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '6':
            tracker.display_expenses()
            try:
                index = int(input("Enter the index of the expense to edit: ")) - 1
                new_date = input("Enter new expense date (YYYY-MM-DD): ")
                try:
                    datetime.strptime(new_date, '%Y-%m-%d')
                except ValueError:
                    print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
                    continue
                new_category = input("Enter new expense category: ")
                new_amount = float(input("Enter new expense amount: "))
                tracker.edit_expense(index, new_date, new_category, new_amount)
            except ValueError:
                print("Invalid input. Please enter the correct data types.")
        elif choice == '7':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

import json

FILE = "expenses.json"


def load_expenses():
    try:
        with open(FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_expenses(expenses):
    with open(FILE, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense(expenses):
    name = input("Expense name: ")

    try:
        amount = float(input("Amount: "))

        if amount <= 0:
            print("Amount must be greater than 0.")
            return

        expenses.append({
            "name": name,
            "amount": amount
        })

        save_expenses(expenses)
        print("✅ Expense saved!")

    except ValueError:
        print("❌ Enter a valid number.")


def show_expenses(expenses):
    if not expenses:
        print("No expenses yet.")
        return

    total = 0

    print("\n--- Expenses ---")

    for expense in expenses:
        print(f"{expense['name']}: ₹{expense['amount']:.2f}")
        total += expense["amount"]

    print(f"Total: ₹{total:.2f}")


def main():
    expenses = load_expenses()

    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add expense")
        print("2. Show expenses")
        print("3. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            show_expenses(expenses)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
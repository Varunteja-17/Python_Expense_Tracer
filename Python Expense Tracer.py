import mysql.connector
import datetime

# ------------------ MySQL Connection ------------------
conn = mysql.connector.connect(
    host="localhost",
    user="root",           
    password="Varunteja@17",
    database="expense_tracker"
)

cursor = conn.cursor()
print("MySQL Connected Successfully\n")

# ------------------ Add Expense ------------------
def add_expense():
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")
    date = datetime.date.today()

    query = """
    INSERT INTO expenses (date, category, amount, description)
    VALUES (%s, %s, %s, %s)
    """
    values = (date, category, amount, description)

    cursor.execute(query, values)
    conn.commit()

    print("\nExpense added successfully!\n")

# ------------------ View Expenses ------------------
def view_expenses():
    cursor.execute("SELECT * FROM expenses")
    records = cursor.fetchall()

    if not records:
        print("No expenses found.\n")
        return

    print("\nID  Date        Category     Amount    Description")
    print("-" * 55)

    for row in records:
        print(f"{row[0]:<3} {row[1]}  {row[2]:<12} ₹{row[3]:<8} {row[4]}")
    print()

# ------------------ Total Expense ------------------
def total_expense():
    cursor.execute("SELECT SUM(amount) FROM expenses")
    total = cursor.fetchone()[0]

    if total is None:
        total = 0

    print(f"\nTotal Expense: ₹{total}\n")

# ------------------ Main Menu ------------------
def menu():
    while True:
        print("Expense Tracker Menu")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expense()
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Try again.\n")

menu()

cursor.close()
conn.close()

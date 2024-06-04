import sqlite3

conn = sqlite3.connect("ExpenseTracker.db")
cur = conn.cursor()

conn.execute("CREATE TABLE IF NOT EXISTS expenses (id INTEGER PRIMARY KEY, date TEXT, category TEXT, amount REAL, explanation TEXT)")
conn.commit()


def AddExpense(date, category, amount, explanation):

    cur.execute("INSERT INTO expenses (date, category, amount, explanation) VALUES (?, ?, ?, ?)", (date, category, amount, explanation))
    conn.commit()


def ViewExpenses():

    cur.execute("SELECT * FROM expenses")
    expenses = cur.fetchall()

    for expense in expenses:
        id, date, category, explanation, amount = expense
        print(f"id: {id}, Date: {date}, Category: {category}, Amount: {amount}, Explanation: {explanation}")



def UpdateExpense(id, NewDate, NewCategory, NewAmount, NewExplanation):

    cur.execute("UPDATE expenses SET date=?, category=?, amount=?, explanation=? WHERE id=?", (NewDate, NewCategory, NewAmount, NewExplanation, id))
    conn.commit()

def DeleteExpense(id):

    cur.execute("DELETE FROM expenses WHERE id=?", (id))
    conn.commit()

while True:
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Update Expenses")
    print("4. Delete Expenses")
    print("5. Exit")

    choice = input("Enter your choice(1, 2, 3, 4 or 5): ")

    if choice == '1':

        date = input("Enter the date (YYYY-MM-DD): ")
        category = input("Enter the category: ")
        amount = float(input("Enter the amount: "))
        explanation = input("Enter the explanation: ")
        
        AddExpense(date, category, explanation, amount)

    elif choice == '2':

        ViewExpenses()

    elif choice == '3':

        id = int(input("Enter your id: "))
        NewDate = input("Enter the new date (YYYY-MM-DD): ")
        NewCategory = input("Enter the new category: ")
        NewAmount = float(input("Enter the new amount: "))
        NewExplanation = input("Enter the new explanation: ")

        UpdateExpense(id, NewDate, NewCategory, NewAmount, NewExplanation)

    elif choice == '4':

        id = int(input("Enter the id you want to delete: "))
        DeleteExpense(id)

    elif choice == '5':
        print("Exited")
        break

print("Expense Tracker")

total = 0
count = 0

while True:
    expense = input("Enter expense amount or type done to finish: ")

    if expense.lower() == "done":
        break

    try:
        expense = float(expense)

        if expense <= 0:
            print("Enter an amount greater than zero")
            continue

        total = total + expense
        count = count + 1

        print("Expense added successfully")
        print("Current total:", total)

    except ValueError:
        print("Invalid input. Please enter a number")

print("\nExpense Summary")
print("Number of expenses:", count)
print("Total spent: Rs.", round(total, 2))
print("Thank you!")
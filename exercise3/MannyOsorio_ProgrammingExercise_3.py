from functools import reduce

def main():
    expenses = {}

    # ask the user for all their expenses
    while True:
        current_expense = input("Enter your expense | enter 'done' when finished: ")

        # check if the user is done inputting expenses
        if current_expense == "done":
            break

        current_amount = input("Enter the amount spent: ")

        expenses[current_expense] = int(current_amount)

    # find the total, max, and min expense
    total_expense = reduce(lambda x,y: x+y, expenses.values()) 

    # find the value of the maximum expense and find its key from the dict
    max_expense = reduce(lambda x,y: max(x,y), expenses.values())
    max_expense_name = None

    for key, value in expenses.items():
        if value == max_expense:
            max_expense_name = key
            break

    # find the value of the minimum expense and find its key from the dict
    min_expense = reduce(lambda x,y: min(x,y), expenses.values())

    for key, value in expenses.items():
        if value == min_expense:
            min_expense_name = key
            break

    # print results
    print(f"The total expense is {total_expense}.")
    print(f"The max expense comes from {max_expense_name} at {max_expense}")
    print(f"The min expense comes from {min_expense_name} at {min_expense}")


if __name__ == "__main__":
    main()
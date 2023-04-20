def display_transactions(transactions):
    for transaction in transactions:
        print(f"${transaction} worth of transactions")


def all_expenses(transactions):
    amount_of_expenses = 0
    for transaction in transactions:
        if transaction < 0:
            amount_of_expenses += transaction
    print(f"Amount of total expenses: ${amount_of_expenses}")


def total_revenue(transactions):
    amount_of_revenues = 0
    for transaction in transactions:
        if transaction > 0:
            amount_of_revenues += transaction
    print(f"Amount of total expenses: ${amount_of_revenues}")

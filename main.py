import bank_account
import helper_functions


jacob_s_bank_account = bank_account.Bank_account("Jacob", 25000, [200000, -14999, -2025, 25573, -5000])

jacob_s_bank_account.account_data()

helper_functions.display_transactions(jacob_s_bank_account.transactions)

helper_functions.all_expenses(jacob_s_bank_account.transactions)

helper_functions.total_revenue(jacob_s_bank_account.transactions)


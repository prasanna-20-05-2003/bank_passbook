from os import system
from passbook_generator import passbook
from welcome_arts import *
from imp_fxns import *

# below fxn takes input of no of transactions and opening balance

no_of_transactions=0;opening_balance = 0;total_balance = 0
transactions_data = {}
transaction_no = 0
exception_during_input=True

while exception_during_input :
    value = basic_input_taker() 
    if value is not None:
        no_of_transactions,opening_balance = value
        total_balance = opening_balance
        exception_during_input=False

while transaction_no < no_of_transactions:

    welcome_to_bank()


    formatting_string = '\n\t\t\t'

    print(formatting_string+'Total Balance:',total_balance)
    print(formatting_string+'Enter choice for transaction:',transaction_no+1)
    transaction_type = float(input('\n\t\t\tType (1.Credit | 2.Debit): '))
    
    
    result_of_transaction = transaction_details(transaction_type,total_balance)

    if result_of_transaction is None:
        continue
    else:
        Status,credit_amount,debit_amount,sign,transaction_time=result_of_transaction

    total_balance+=(credit_amount+debit_amount)*sign
    transaction_no+=1

    transactions_data[transaction_no] = {
        'Status':Status,
        'Credit':str(credit_amount),
        'Debit':str(debit_amount),
        'Total':str(total_balance),
        'Time':transaction_time,
    }

    system('cls')

welcome_to_passbook(bank_name,opening_balance)
passbook(transactions_data)
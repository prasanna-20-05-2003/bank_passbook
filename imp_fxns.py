from time import sleep,asctime
from os import system
from welcome_arts import welcome_to_bank,center_string

def invalid_amt_msg(amount,type):
    if amount == 0:
            print(f'\n\t\t\tYou can\'t enter 0.0 are {type} amount!')
    elif amount < 0:
            print(f'\n\t\t\tYou entered a negative amount for {type}.')
    sleep(4)
    system('cls')

def is_DebitAmt_higher(debit_amt,total_balance):


    if debit_amt > total_balance:
        print('\n\t\t\tInsufficient funds!!')
        sleep(4)
        system('cls')
        return True
    else:
        return False

def basic_input_taker():

    system('cls')
    print('\n')
    welcome_to_bank()

    no_of_transactions = int(input('\n\t\t\tEnter the no of transactions you want to make: '))
    if no_of_transactions < 0:
        print('\n\t\t\tInvalid number for number of transactions entered');sleep(4)
        return None

    opening_balance = float(input('\n\t\t\tEnter the total balanace in your account: '))
    if opening_balance < 0:
        print('\n\t\t\tBalance cannot be negative!');sleep(4)
        return None
    system('cls')
    return no_of_transactions,opening_balance
    
def transaction_details(transaction_type,total_balance):
        
        formatting_string = '\n\t\t\t'

        if transaction_type == 1.0:
                
                amount = float(input(formatting_string+'Enter the amount to be deposited: '))
                if amount <= 0:
                        invalid_amt_msg(amount,'credit')
                        return None
                else:
                        return 'Cr',amount,0,1,asctime() # status credit_amt debit_amt sign
        elif transaction_type == 2.0:
                amount = float(input(formatting_string+'Enter the amount to be withdrawn: '))
                if amount <= 0:
                        invalid_amt_msg(amount,'debit')
                        return None
                elif is_DebitAmt_higher(amount,total_balance):
                        return None
                else:
                        return 'Dr',0,amount,-1,asctime()
        else:
                print(f'{formatting_string}Invalid number for transaction type entered! Type 1 or 2')
                sleep(4)
                system('cls')
                return None

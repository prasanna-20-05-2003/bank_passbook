def center_string(allowed_num_characters,string,end_string=''):

     total_space = allowed_num_characters-len(string)
     space_in_front = total_space // 2
     space_in_back = total_space - space_in_front
     return f'{" "*space_in_front}{string}{" "*space_in_back}' + end_string 

initial_passbook = '''
\t\t ______________________________________________________________________________________________
\t\t|                                                                                              |
\t\t|**********************************************************************************************|
\t\t|                                                                                              |
'''

middle_passbook = '''
\t\t|                                                                                              |  
\t\t|**********************************************************************************************|
\t\t|______________________________________________________________________________________________|
\t\t|                                                                                              |
'''

final_passbook='''
\t\t|                                                                                              |
\t\t|++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++|
\t\t|            |                |               |                 |                              |
\t\t|$$$STATUS$$$|$$$$$CREDIT$$$$$|$$$$$DEBIT$$$$$|$$$$$$TOTAL$$$$$$|$$$$$$$$$$$$$TIME$$$$$$$$$$$$$|
\t\t|            |                |               |                 |                              |  
\t\t|++++++++++++|++++++++++++++++|+++++++++++++++|+++++++++++++++++|++++++++++++++++++++++++++++++|
\t\t|            |                |               |                 |                              |\
'''

final_passbook = final_passbook.replace('$',' ')
bank_name = "ICICI BANK"

def welcome_to_bank():

        print(f'''\n\n
\t\t    |+++++++++++++++++++++++++++++++++++++++++++++++++++++++++|
\t\t    |                                                         |
\t\t    |                                                         |\
''')
        bank_name_in_box = '\t\t    |'+center_string(57,bank_name)+'|'
        print(bank_name_in_box)
        print('''\
\t\t    |                                                         |
\t\t    |                                                         |
\t\t    |+++++++++++++++++++++++++++++++++++++++++++++++++++++++++|
''')
        
def welcome_to_passbook(bank_name,op_bal):

    print(initial_passbook,end='')
    bank_name_msg = f'{bank_name} - PASSBOOK DETAILS'
    print('\t\t|'+center_string(94,bank_name_msg)+'|',end='')
    print(middle_passbook,end='')
    opening_balance_msg = f'OPENING BALANCE: {op_bal}' 
    print('\t\t|'+center_string(94,opening_balance_msg)+'|',end='')
    print(final_passbook)
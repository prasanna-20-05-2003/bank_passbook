from imp_fxns import center_string 

def passbook(transactions):
    allowed_characters = [12,16,15,17,30]
    empty_line = '\t\t'
    for i in allowed_characters:
        empty_line+='|'+'-'*i
    empty_line+='|'
    feilds = ['Status','Credit','Debit','Total','Time']
    for transaction_no in range(1,len(transactions)+1):
        print('\t\t',end='')
        for j in range(5):
            string=center_string(allowed_characters[j],transactions[transaction_no][feilds[j]])
            if j < 4:
                print(f'|{string}',end='')
            else:
                print(f'|{string}|',end='')
        print()
        if transaction_no < len(transactions):
            print(empty_line)
        else:
            print(empty_line.replace('-','_'))
    print('\n')
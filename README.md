THE BANK PASSBOOK WILL BE DISPLAYED AFTER SET OF TRANSACTIONS DONE BY THE USER

MAIN FILE SHOULD BE RUN TO SEE OUTPUT AND OTHER PYTHON FILES ARE MODULES WHICH CONTAINS FUNCTIONS,VARIABLES 

_______________________________________________________________________________________________________________

Modules in this project are :


      1. " WELCOME_ARTS MODULE " 
      
      Which Contains Welcome To Bank Fxn And Welcome To Passbook Fxn

      2. " IMP_FXNS MODULE "
      
      Which Contains Basic Input Taker Fxn (Which Basically Takes Initial Inputs Of
      No Of Transactions And Opening Balance) , Fxn To Take Input Of Transaction Details For Each Transaction
      And Some Fxns For Exception Handling

      3. " PASSBOOK_GENERATOR MODULE " 
      
      Which Loops Through The Transactions Data And Prints Out Value Of
      Various Feilds For Each Transaction Into The Terminal 
      
_______________________________________________________________________________________________________________

For each transaction :

      1. The user is asked whether he wants to credit / debit

      2. And also the amount is taken as input

______________________________________________________________________________________________

After all the transactions are completed :

      1. A passbook is printed which contain these feilds

      2. Status , Credit , Debit , Total balance, Time  (for each transaction)
      
_____________________________________________________________________________________________

Exception handling has been done for the following cases :

      1. If no of transactions entered by user is negative

      2. If balance entered is negative

      3. If debit_amount > available balance

      4. If debit_amount or credit_amount is zero or negative

      5. If invalid option number (like 3) is entered when we ask for transaction type (Dr or Cr)

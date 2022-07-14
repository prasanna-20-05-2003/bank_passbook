THE BANK PASSBOOK WILL BE DISPLAYED AFTER SET OF TRANSACTIONS DONE BY THE USER

MAIN FILE SHOULD BE RUN AND IT GETS THE NO OF TRANSACTIONS AND OPENING BALANCE AS USER INPUT

_______________________________________________________________________________________________________________

MODULES USED IN THIS PROJECT ARE:

      1.WELCOME_ARTS MODULE WHICH CONTAINS WELCOME TO BANK FXN AND WELCOME TO PASSBOOK FXN
      
      2.IMP_FXNS MODULE WHICH CONTAINS BASIC INPUT TAKER FXN (WHICH BASICALLY TAKES INITIAL INPUTS OF
      NO OF TRANSACTIONS AND OPENING BALANCE) , FXN TO TAKE INPUT OF TRANSACTION DETAILS FOR EACH TRANSACTION
      AND SOME FXNS FOR EXCEPTION HANDLING
      
      3.PASSBOOK_GENERATOR MODULE WHICH LOOPS THROUGH THE TRANSACTIONS DATA AND PRINTS OUT VALUE OF
      VARIOUS FEILDS FOR EACH TRANSACTION INTO THE TERMINAL 
      
_______________________________________________________________________________________________________________

After which for each transaction :

      1. The user is asked whether he wants to credit / debit

      2. And also the amount is taken as input

______________________________________________________________________________________________

After all the transactions are completed , 

      1. A passbook is printed which contain these feilds

      2. Status , Credit , Debit , Total balance, Time  (for each transaction)
      
_____________________________________________________________________________________________

Exception handling has been done for the following cases:

      1. If no of transactions entered by user is negative

      2. If balance entered is negative

      3. If debit_amount > available balance

      4. If debit_amount or credit_amount is zero or negative

      5. If invalid option number (like 3) is entered when we ask for transaction type (Dr or Cr)

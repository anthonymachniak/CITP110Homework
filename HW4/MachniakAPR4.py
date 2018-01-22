##############################################################################################
#### 1) HW 4: ATM Transactions
#### 2) Anthony Machniak
#### 3) 9/25/17
#### 4) The user inputs their name, account number, and what they want done to the account.
####    Processes are withdrawal, deposit, and display balance.
##############################################################################################


def main():
    Name = input('Please enter your name: ')
    Account_ID = input('Please enter your account ID: ')

    Transaction_Input()


def Transaction_Input():
    Transaction_Code = input("Please enter 'W' for withdrawal or 'D' for deposit. ")
    Transaction_Code_List = ["W", "w", "D", "d"]

    while Transaction_Code not in Transaction_Code_List:
        print("Invalid Transaction Code.")
        Transaction_Code = input("Please enter 'W' for withdrawal or 'D' for deposit. ")
    
    
    Previous_Balance = float(input('Please enter your previous balance: '))

    if Transaction_Code == "W" or Transaction_Code == "w":
        Transaction_Amount = float(input("Please enter the amount you want to withdraw: "))
        Withdrawal(Previous_Balance, Transaction_Amount)
    else:
        Transaction_Amount = float(input("Please enter the amount you want to deposit: "))
        Deposit(Previous_Balance, Transaction_Amount)



def Withdrawal(Previous_Balance, Transaction_Amount):
    if Previous_Balance >= Transaction_Amount:
        New_Balance = Previous_Balance - Transaction_Amount
        Display_Balance(New_Balance)
        Continue_Transaction()
    else:
        print("Invalid Transaction: Insufficient Funds")
        Display_Balance(Previous_Balance)
        Transaction_Input()


def Deposit(Previous_Balance, Transaction_Amount):
    New_Balance = Previous_Balance + Transaction_Amount
    Display_Balance(New_Balance)
    Continue_Transaction()


def Display_Balance(New_Balance):
    print("Your current balance is: $", format(New_Balance, '.2f'))


def Continue_Transaction():
    Continue = input("Do you wish to make another transaction? Enter 'Y' for yes or 'N' for no. ")
    
    if Continue == "Y" or Continue == "y":
        print("")
        Transaction_Input()
    elif Continue == "N" or Continue == "n":
        quit()
    else:
        Continue_Transaction()


main()

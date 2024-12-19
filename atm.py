import time 
import os
import mysql.connector
from mysql.connector import Error
from  sqlalchemy import create_engine

con=mysql.connector.connect(host='127.0.0.1',user='root',password='root',database='atm')

if con.is_connected():
        cursor = con.cursor()
def log_transaction(transaction_type,amount,current_balance):
   time_stamp=time.strftime('%Y-%m-%d %H:%M:%S')
   query='''insert into transaction (transaction_type,amount,current_balance,time_stamp)
   values(%s,%s,%s,%s)'''
   cursor.execute(query,(transaction_type,amount,current_balance,time_stamp))
   con.commit()
   return "Transaction logged successfully"

def get_balance():
    query = "SELECT current_balance FROM transaction ORDER BY time_stamp DESC LIMIT 1"
    cursor.execute(query)
    result = cursor.fetchone()
    return result[0] if result else 1000

def view_transaction_log():
    query = "SELECT * FROM transaction"
    cursor.execute(query)
    result = cursor.fetchall()
    print(' ID | Transaction_Type | Amount | Current_Balance | Time_Stamp ')
    for row in result:
        print(row)

os.system('cls')
c=0
print('-------😊 Welcome to Bank of Barodra 😊-------')
while True:
    PIN=input('Enter your 4 digit pin:')
    time.sleep(1)
    if len(PIN)==4 and PIN.isdigit() and PIN[0]!='0':
        PIN=int(PIN)
        break
    else:
        c+=1
        print("Invalid PIN. Ensure it is a 4-digit number that doesn't start with 0.")
        if c>=3:
            print('You have crossed limited attempt to enter pin')
            break

print('Please Choose your account type')
print('1. Savings Account')
print('2. Current Account')
print('3. Fixed Deposit')
print('4. Change PIN')
print('5. View Transaction Log')
account_type=int(input('Enter your choice:'))
balance=get_balance()
transaction_log=[]
time.sleep(1)
    
if account_type==1:
    os.system('cls')
    print('You have chosen Savings Account')
    print('Enter your choice:')
    print('1. Deposit')
    print('2. Withdraw')
    print('3. Check Balance')
    choice=int(input('Enter your choice:'))
    if choice==1:
        amount=float(input('Enter the amount to deposit:'))
        balance+=amount
        log_transaction('Saving_Account Deposite',amount,balance)
        print('Amount Deposite Sucessfully')
        time.sleep(2)
        print('Do you want to check balance:')
        print('1. Yes')
        print('2. No')
        a=int(input('Enter your choice:'))
        c=0
        while True:
                ch=int(input('ReEnter PIN:'))
                time.sleep(1)
                if ch!=PIN:
                    c+=1
                    if c>3:
                        print('INVALID PIN\nPLZ CONTACT IN YOUR BANK')
                        break
                else:
                    print('Your current balance is ₹',balance)
        if a==1:
            print('Your current balance is ₹',balance)
        elif a==2:
                exit
        else:
            print('Invalid choice')
                
    elif choice==2:
            amount=float(input('Enter the amount to withdraw:'))
            if amount>balance:
                print('Insufficient balance')
            else:
                balance-=amount
                log_transaction('Saving_Account Withdraw',amount,balance)
                print('Under Processing')
            time.sleep(2)
            print('Amount withdrawn successfully')
            print('Do you want to check balance:')
            print('1. Yes')
            print('2. No')
            choice=int(input('Enter your choice:'))
            c=0
            while True:
                ch=int(input('ReEnter PIN:'))
                time.sleep(1)
                if ch!=PIN:
                    c+=1
                    if c>3:
                        print('INVALID PIN\nPLZ CONTACT IN YOUR BANK')
                        break
                else:
                    break
            if choice==1:
                    print('Your current balance is:',balance)
            elif choice==2:
                    exit
    elif choice==3:
        print('Your current balance is:',balance)
    else:
            print('Invalid choice')  
            
            
elif account_type==2:
    os.system('cls')
    print('1. Deposit')
    print('2. Balance Inquiry')
    print('3. Fund Transfer')
    ch=int(input('Enter your choice:'))
    if ch==1:
        amount=int(input('Enter the amount to deposit:'))
        balance+=amount
        print('Amount Deposited Successfully')
        log_transaction('Current_Account Deposite',amount,balance)
        time.sleep(2)
        os.system('cls')
        print('Do you want to check balance:')
        print('1. Yes')
        print('2. No')
        choice=int(input('Enter your choice:'))
        if choice==1:
            print('Your current balance is:',balance)
        elif choice==2:
            exit
    elif ch==2:
            print('Your current balance is:',balance)
    elif ch==3:
        print('1.Same Bank Transfer\n2.InterBank Transfer')
        choice=int(input('Enter your choice:'))
        if choice==1:
            print('Enter the account number of the recipient:')
            recipient_account_number=int(input('Enter the account number:'))
            time.sleep(2)
            pin=int(input('Enter PIN:'))
            if pin==PIN:
                    print('Enter the amount to transfer:')
                    amount=int(input('Enter the amount:'))
                    if amount>balance:
                        print('Insufficient balance')
                    else:
                        balance-=amount
                        print('Amount transferred successfully')
                        log_transaction('Same Bank Transfer',amount,balance)
            else:
                print('Invalid PIN')
        elif choice==2:
            print('Enter the account number of the recipient:')
            recipient_account_number=int(input('Account number:'))
            print('Enter the IFSC code of the recipient bank:')
            recipient_ifsc_code=input('IFSC code:')
            pin=int(input('Enter Your PIN:'))
            time.sleep(1)
            if pin==PIN:
                print('Enter the amount to transfer:')
                amount=int(input('Amount:'))
                if amount>balance:
                    print('Insufficient balance')
                else:
                    balance-=amount
                    print('Amount transferred successfully')   
                    log_transaction('InterBank Transfer',amount,balance)
            else:
                print('Invalid PIN')


elif account_type==3:
    print('Your Account Type is not : Fixed Deposite')


elif account_type==4:
    ch=int(input('Plz Enter Your Previous Pin:'))
    c=0
    while True:
        ch=int(input('ReEnter PIN:'))
        time.sleep(1)
        if ch!=PIN:
            c+=1
            if c>3:
                print('INVALID PIN\nPLZ CONTACT IN YOUR BANK')
                break
        else:
                break
    if ch==PIN:
        time.sleep(1)
        new_pin=int(input('Enter New Pin:'))
        PIN=new_pin
        time.sleep(2)
        print('PIN Changed Succesfully')
        exit

elif account_type==5:
    os.system('cls')
    view_transaction_log()

else:
    print('Invalid Account Type')
    exit

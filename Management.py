import sys
class Customer:
    """customer class with bank operations."""
    bankname="StateBank"
    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance

    def deposit(self,amount):
        self.balance=self.balance+amount

    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient Balance")
            sys.exit()

        self.balance=self.balance-amount
        print("The Balance after withdraw: ",self.balance)
print("Welcome to ",Customer.bankname)
name=input("Enter the Customer Name:")
c=Customer(name)
while True:
    print('d-deposit \n w-Withdraw \n e-exit')
    option=input("Choose your option: ")
    if option.lower()=='d':
        amount=eval(input("enter amount to deposit: "))
        c.deposit(amount)

    elif option.lower()=='w' :

        amount=eval(input("enter amount to withdraw: "))
        if amount>10000:
            print("You can't exceed the limit of Rs 10,000")
        elif amount%100==0 or  amount%2000==0 or amount%500==0 :
            c.withdraw(amount)

        elif amount%100!=0 or  amount%2000!=0 or amount%500!=0 :
            print("Enter the amount in the multiple of 100,500,and 2000")
        elif amount<100:
            print("You can withdraw greater than 100 rupee")

    elif option.lower()=='e':
        print("Thank you for banking")
        sys.exit()
    else:
        print("invalid option")








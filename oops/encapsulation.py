class BankAccount:
    def __init__(self):
        self.__bank_balance = 0

    def deposit(self):
        amount = int(input("Enter the deposite amount amount: "))
        if amount == 0 or amount <  0:
            print("Cannot deposit")
            return False 
        self.__bank_balance = amount
        print(f"✅ Amount ${amount} deposited successfully")
        return True 
    
    def withdraw(self):
        amount = int(input("Enter the withdrawal amount the amount: "))
        if amount > self.__bank_balance:
            print("Insufficient balance!")
            return False
        self.__bank_balance -=amount
        print(f"✅ Amount ${amount} withdrawed successfully")
        return True
    
    def get_balance(self):
        print(f"Total Balance ${self.__bank_balance}")


account = BankAccount()
account.deposit()
account.withdraw()
account.get_balance()
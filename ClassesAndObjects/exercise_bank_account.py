#Create a class BankAccount with attributes: owner, balance

#Add methods to: deposit money, withdraw money, display the balance

class BankAccount:

    def __init__(self, owner:str, balance:float):
        
        self.owner = owner
        self.balance = balance
    
    #Method to deposit 
    def deposit(self, add_value):
        if add_value >= 0:
            self.balance += add_value
        return self.balance
                


    #Method to Withdraw
    def withdraw(self, remove_value):
        if remove_value:
            self.balance -= remove_value
        return self.balance


    #Method to display balance
    def __str__(self):
        if BankAccount.deposit:
            return f"{self.owner}'s current account value is {self.balance}"
        elif BankAccount.withdraw:
            return f"{self.owner}'s current account value is {self.balance}"
        else:
            return f"{self.owner}'s current  account value is ${self.balance}"


def main():
    account1 = BankAccount("John", 1000.00)
    print(account1)

    account1.deposit(100)
    print(account1)

    account1.withdraw(500)
    print(account1)


if __name__ == '__main__':
    main()


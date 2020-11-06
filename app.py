class BankAccount:
    def __init__(self, full_name, account_number, routing_number, balance):
        self.full_name = full_name
        self.account_number = account_number
        self.routing_number = routing_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("\n Amount Deposited:", amount)

        # Function to withdraw the amount
    def withdraw(self, amount):
        amount = float((input("Enter a amount")))
        if self.balance >= amount:
            self.balance -= amount
            print("\n You Withdrew", amount)
        else:
            print("\n Insufficient funds.")
            self.balance - 10
        # Function to display the amount

    def display_balance(self):
        print("\n You have ", self.balance)

    def add_interest(self, balance):
        interest = self.balance * 0.00083

    def print_receipt(self):
        print(self.full_name)
        print("Account Number: " + str(self.account_number))
        print("routing number: " + str(self.routing_number))
        print("balance:" + str(self.balance))


# creating an object of class
customer1 = BankAccount('Alex', 000000, 000000, 10)
customer1.deposit(100)
customer1.withdraw(50)
customer1.display_balance
# customer1.add_interest
customer1.print_receipt()

customer2 = BankAccount('Bob', 3121212, 21212121, 10000)
customer2.deposit(100)
customer2.withdraw(50)
customer2.display_balance
# customer1.add_interest
customer2.print_receipt()

customer2 = BankAccount('John', 312221212, 212121321, 1000)
customer2.deposit(222)
customer2.withdraw(50)
customer2.display_balance
# customer1.add_interest
customer2.print_receipt()

# Calling functions with that class object
# Calling functions with that class object

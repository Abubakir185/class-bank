class Customer:
    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = balance
    
    def show_balance(self):
        print(self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Mablag' yetarli emas!")
        

    def deposite(self, amount):
        self.balance += amount
    
    def transfer(self, another_customer, amount):
        if amount <= self.balance:
            another_customer.withdraw(amount)
            another_customer.deposite(amount)
            print(f"{another_customer}ga {amount}sum otqazildi, balance -> {self.balance}")
        else:
            print("Mablag' yetarli emas!")

    def __str__(self):
        return f"name: {self.name}, balance: {self.balance}"
        


class Bank:
    def __init__(self):
        self.customers = []
        self.total_balance = 0


    def add_customer(self, name, balance):
        self.customers.append(name)
        self.total_balance += balance
        return f"{name} bankga qoshildi!"
    
    
    def find_customer(self, name):
        if name in self.customers:
            print(name)
        else:
            print("Bunday isimli mijoz yoq.")
        
    def delete_customer(self, name):
        index = self.customers.index(name)
        self.customers.pop(index)
        

    def list_of_customers(self):
        print(self.customers)
    

    def check_total_balance(self):
        print(self.total_balance)






# john = Customer("John", 20)
# tom = Customer("Tom", 30)
   
# john.transfer(tom, 10)
# john.show_balance()
# tom.show_balance()
# print(tom)

bank = Bank()
abu = bank.add_customer("Abu", 100000)
john = bank.add_customer("John", 200000)
bank.find_customer("Abu")
# bank.list_of_customers()
# bank.delete_customer(abu)
# bank.list_of_customers()
# bank.check_total_balance()











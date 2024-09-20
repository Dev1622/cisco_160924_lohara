class Account:
    def __init__(self,number,name,initial_amount = 1000):
        self.__number = number
        self.__name = name
        self.__balance = initial_amount

    """ def __repr__(self):
        return(f'number={self.__number},name={self.__name},balance={self.__balance}')
    
    def __str__(self):
        return self.__repr__() """
    def __str__(self):
        return(f'number={self.__number},name={self.__name},balance={self.__balance}')
    
    def __repr__(self):
        return self.__str__()
    
    def deposit(self,amount):
        if amount < 0:
            print('The amount cannot be negative')
            return
        self.__balance += amount
        
    def withdraw(self,amount):
        if amount > self.__balance:
             print('No enough balance')
             return 
        self.__balance -= amount

rohit_ac = Account(name='Rohit',number='1344000000045',initial_amount=3000)
print(rohit_ac)

rohit_ac.deposit(-200000)
print(rohit_ac)

rohit_ac.withdraw(3000)
print(rohit_ac)
#debit = rohit_ac.withdraw()

#print(rohit_ac.__dict__)

rohit_ac.withdraw(210000)
print(rohit_ac)
 
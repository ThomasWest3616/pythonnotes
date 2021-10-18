# https://python-elective-kea.github.io/fall2021/ses7.html

class Bank:
    def __init__(self):
        self.accounts = []

    @property
    def accounts(self):
        return self.__accounts

class Account:
    def __init__(self, no, cust):
        self.no = no
        self.cust = cust
    
    @property
    def no(self):
        return self._no
    
    @property
    def cust(self):
        return self._cust

class Customer:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name
    
    @property
    def age(self):
        return self._age

    
    @age.setter
    def customer(self, new_age):
        if new_age > 18 and isinstance(new_age, int): 
            self._age = new_age
        else:
            print("You must be over 18 year old")


customer1 = Customer("Hej", 10)
customer2 = Customer("Thomas", 20)

print(customer1)
print(customer2)
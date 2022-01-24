METHODS = ['stripe', 'paypal', 'mobilepay']

class Payment:
    def __init__(self, method):
        self.__method = method

    @property
    def method(self):
        return self.__method

    @method.setter
    def method(self, met):
        if(met in METHODS):
            self.__method = met

    @method.deleter
    def method(self):
        print("Deleting")
        self.__method = ''


pay = Payment('stripe')
pay.method = 'mobilepay'
print(pay.method)
del pay.method

print(pay.method)
class Payment:
    def __init__(self, price):
        # self.final_price = price + price *0.05 # Dette er public, vi skal gøre det private
        # self._final_price = price + price *0.05 # Private ved at lave _ som en slags "warning"
        self.__final_price = price + price*0.05  # __ for at gøre den private og ingen kan røre den

    def get_final_price(self): # Getter via en wrapper og sørger for at man ikke kan ændre værdien
        return self.__final_price

    def set_final_price(self, discount): # Setter hvis man nu f.eks. har en coupon
        self.__final_price = self.__final_price - (self.__final_price * (discount/100))



    
book = Payment(10)
book.set_final_price(10)

book.__final_price = 0 # Kan ikke ændres da attribute er private

# book.final_price = 0 # Undgå dette
# book._final_price = 0 # Private kan ikke ændres
# book.__final_price = 0 # Vil give fejl pga. __

print(book.get_final_price())


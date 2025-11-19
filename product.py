from base import BaseModel


class Product(BaseModel):
    _next_id = 1

    def __init__(self,name, price, description, quantity ):
        super().__init__(name)
        self._price = price
        self._description = description
        self._quantity = quantity
    

    @property
    def price(self):
        return self._price
    
    @property
    def description(self):
        return self._description
    
    @property
    def quantity(self):
        return self._quantity
    
    @price.setter
    def price(self, pValue):
        if pValue <= 0 :
            raise ValueError("Price Can't be less than 0 ")
        self._price = pValue

    @description.setter
    def price(self, dValue):
        self._description = dValue

    @quantity.setter
    def price(self, qValue):
        self.quantity = qValue     


    def __str__(self):
            return (
                f"{self.__class__.__name__}("
                f"id={self._id}, "
                f"name={self._name}, "
                f"price={self._price}, "
                f"description={self._description}, "
                f"quantity={self._quantity}"
                f")"
            )
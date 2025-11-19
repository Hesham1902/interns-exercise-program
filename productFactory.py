from product import Product

class ProductFactory():
    @staticmethod
    def create(name, price, description, quantity):
        return Product(name, price, description, quantity)
    


p = ProductFactory.create("p",34,"Ddd",4)
print(p)    
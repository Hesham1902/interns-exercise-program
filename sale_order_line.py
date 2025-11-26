from base import BaseModel
class SaleOrderLine(BaseModel):
    def __init__(self, product, quantity):
        super().__init__(f"line- {product.name}")
        self._product=product
        self._quantity=quantity
        self.price=product.price
        self.subtotal= self.price*self._quantity
    def __str__(self):
        return (
    f"SaleOrderLine(id={self._id}, product={self._product.name}, "
    f"quantity={self._quantity}, unit_price={self.price}, subtotal={self.subtotal})"
)

   
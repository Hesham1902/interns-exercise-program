from base import BaseModel
from sale_order_line import SaleOrderLine
from Invoice import Inovice


class SaleOrder (BaseModel):
    def __init__(self, name ,customer):
        super().__init__(name)
        self._customer=customer
        self._lines=[]
        self.state="draft"
        self.invoice= None

    @property
    def lines(self):
        return self._lines
    
    def add_line(self,product,quantity):
        if quantity <=0:
         raise ValueError ("quantity must be > 0 ")
        line =SaleOrderLine(product,quantity)
        self._lines.append(line)
        return line 
    
    def confirm(self):
        if self.state != "draft":
            raise ValueError("Order is already confirmed")
        if not self._lines:
            raise ValueError("Cannot confirm an empty order")

        self.state = "confirmed"
        inv= Inovice(f"inv-{self._id}",self._customer)
        for line in self._lines:
            inv.add_line(line.product,line.quantity,line.price)
        self.invoice =inv
        self._customer.add_order(self)
        self._customer.add_invoice(inv)
        return inv
    

    def total_amount(self):
        return sum(line.subtotal for line in self._lines)
    
    def __str__(self):
        return f"SaleOrder(id={self._id}, name={self._name}, state={self.state}, lines={len(self._lines)})"



 


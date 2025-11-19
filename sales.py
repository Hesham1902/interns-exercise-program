from base import BaseModel

class SaleOrder(BaseModel):
   
    
    def __init__(self,state,customer_id):
        self._lines=[]

    def add_line(self,product, quantity):
        new_line = SaleOrderline(product, quantity)
        self._lines.append(new_line)
        return new_line
        

    def confirm():
        pass
        
    

class SaleOrderline():

    def __init__(self,product,quantity,unite_price,sub_total):
        pass


class product(BaseModel):
    def __init__(self, name,id,price,disc,stock_quantity):

    pass


# orderline2 = SaleOrderline(5,20,700,78878)
# orderline3 = SaleOrderline(9,20,600,10000)



    
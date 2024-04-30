class Store : 
    def __init__(self,name) :
        self.name = name 
        self.product = [] 

    def add_Product(self,new_Product):
        self.product.append(new_Product)
        return self 
    
    def sell_product(self, id):
        c = -1
        for i in range(len(self.product)):
            if(self.product[i].id == id):
                c = i 
                break 
        if (c != -1):    
             self.product.pop(c)
        else: 
            print("Error : There is no product with ID",id)     
        return self   

    def inflation(self, rate=.3): 
        for i in range(len(self.product)):
            self.product[i].update_price(rate,True)

    def clearance(self, rate=.3): 
        for i in range(len(self.product)):
            self.product[i].update_price(rate,False)        
             
    def print_allProduct(self):
        for i in self.product:
            i.print_info()
        return self    
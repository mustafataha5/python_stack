class Product:
    count= 100
    def __init__(self,name,price,category):
        self.name=name
        self.price=price
        self.category = category
        self.id = Product.count
        Product.count = Product.count+1 

    def print_info(self):
        print("Name: ",self.name,f" id: {self.id} "," Price: ",self.price," Caregory",self.category)    

    def update_price(self, percent_change, is_increased):
        if(is_increased):
            self.price = self.price+ self.price*percent_change
        else: 
            self.price = self.price- self.price*percent_change    


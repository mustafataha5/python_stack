
import Product  as product
import Store as store



mystore = store.Store("MyStre")

p0 = product.Product("P0",20,"C0")
p1 = product.Product("P1",10,"C2")
p2 = product.Product("P2",25,"C3")
p3 = product.Product("P3",15,"C6")

mystore.add_Product(p0).add_Product(p1).add_Product(p2).add_Product(p3).print_allProduct()
print("----------Update P0 price by  .5 rate ")
mystore.product[0].update_price(.5,True)
mystore.print_allProduct()
print("----------Sell Product  with ID 101")
mystore.sell_product(101)
mystore.print_allProduct()
print("----------Sell Product with ID 105")
mystore.sell_product(105)
mystore.print_allProduct()
print("----------make inflation by .4 rate")
mystore.inflation(.4)
mystore.print_allProduct()
print("----------make clearance by .2 rate")
mystore.clearance(.2)
mystore.print_allProduct()
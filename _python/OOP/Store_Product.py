
import Product  as p
import Store as s



store = s.Store("MyStre")

p0 = p.Product("P0",20,"C0")
p1 = p.Product("P1",10,"C2")
p2 = p.Product("P2",25,"C3")
p3 = p.Product("P3",15,"C6")

store.add_Product(p0).add_Product(p1).add_Product(p2).add_Product(p3).print_allProduct()
print("----------Update P0 price by  .5 rate ")
store.product[0].update_price(.5,True)
store.print_allProduct()
print("----------Sell Product  with ID 101")
store.sell_product(101)
store.print_allProduct()
print("----------Sell Product with ID 105")
store.sell_product(105)
store.print_allProduct()
print("----------make inflation by .4 rate")
store.inflation(.4)
store.print_allProduct()
print("----------make clearance by .2 rate")
store.clearance(.2)
store.print_allProduct()
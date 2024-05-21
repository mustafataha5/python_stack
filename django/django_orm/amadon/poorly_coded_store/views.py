from django.shortcuts import render,redirect
from .models import *
from django.db.models import Sum




def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request):
    if request.method == "POST" :
        quantity_from_form = int(request.POST["quantity"])
        productID= int(request.POST["product"])
        product = Product.objects.get(id=productID)
        price_from_form = float(product.price)
        total_charge = quantity_from_form * price_from_form
        print("Charging credit card...")
        order = Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)     
    
    
        request.session['orderID'] = order.id
        request.session['price'] = price_from_form
        request.session['total_charge'] = float(Order.objects.aggregate(Sum('total_price')).get('total_price__sum'))
        request.session['total_item'] = float(Order.objects.aggregate(Sum('quantity_ordered')).get('quantity_ordered__sum'))
        
        return redirect('/show')
        
def show_order(request):  
    if not 'orderID' in request.session : 
        request.session['orderID'] = ''
        request.session['price'] = 0
        request.session['total_charge'] = 0
        request.session['total_item']=0
    
    data={
        "order":Order.objects.get(id=request.session['orderID'])
    }    
           
    return render(request, "store/checkout.html",data)
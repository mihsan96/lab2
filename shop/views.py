from django.shortcuts import render
from datetime import datetime
from .models import Product, Purchase


# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'shop/index.html', context)


def purchase(request):
    post = request.POST
    purchase_dict = {}
    context = {'purchase': []}
    for p in post:
        if 'quantity' in p:
            if post[p]:
                purchase_dict['product_id'] = p.split(' ')[1]
                purchase_dict['quantity_purchased'] = post[p]
                purchase_dict['address'] = post['address']
                purchase_dict['person'] = post['person']
                product = Product.objects.get(id=p.split(' ')[1])
                purchase_dict['price'] = product.price
                if product.quantity_on_stock < int(post[p]):
                    return render(request, 'shop/error.html')
                Product.objects.filter(id=p.split(' ')[1]).update(
                    quantity_on_stock=product.quantity_on_stock - int(post[p]))
                if product.quantity_on_stock / 2 < int(post[p]):
                    Product.objects.filter(id=p.split(' ')[1]).update(price=product.price * 1.2)
                Purchase.objects.create(**purchase_dict)
                context['purchase'].append(purchase_dict | dict(name=product.name))
    return render(request, 'shop/purchase.html', context)

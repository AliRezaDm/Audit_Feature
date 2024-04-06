from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView
from .models import Cart
from goods.models import Supply
from django.contrib.auth.decorators import login_required
from django.contrib import messages


class CartDetail(DetailView):
    
    model = Cart
    template_name = 'cart/cart_detail.html'

def cart_add(request, product_id):

    item = Cart.objects.filter(user=request.user, product=product_id).first()

    if Supply.objects.get('count') == 0 :
        messages.error(request, 'موجودی محصول کافی نیست')
        return redirect('cart:cart_detail')

    else:

        if item:
            item.quantity +=1
            item.save()
            messages.success(request, 'با موفقیت افزوده شد')
        else:
            Cart.objects.create(user=request.user, product=product_id)
            messages.success(request, 'با موفقیت افزوده شد')

    return redirect('cart:cart_detail')

def cart_remove(request, item_id):

    item = get_object_or_404(Cart, id = item_id)

    if item.user == request.user:
        item.delete()
        messages.success(request,'محصول از سبد خرید حذف شد')
    
    return redirect('cart:cart_detail')


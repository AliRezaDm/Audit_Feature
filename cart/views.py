from django.http import HttpResponseRedirect
from django.views.generic import ListView
from .models import Cart, CartItem
from django.views.decorators.http import require_POST
from django.contrib.auth.mixins import LoginRequiredMixin





class CartListView(ListView, LoginRequiredMixin):
    
    model = Cart
    template_name = 'cart/cart_detail.html'


@require_POST
def add_cart(request):

    url = request.META.get('HTTP_REFERER')
    variant_id = request.POST.get('variant_id')
    variant_quantity = request.POST.get('quantity')
    cart_user = Cart.objects.get(user__id=request.user.id)
    cart_items = CartItem.objects.get(cart__id=cart_user, variant__id=variant_id)   

    if cart_items:
        cart_items.quantity += variant_quantity 
        cart_items.save()
    else:
        CartItem.objects.create(cart__id=cart_user, variant__id=variant_id, quantity = variant_quantity)

    return HttpResponseRedirect(url)

@require_POST
def remove_cart(request):

    url = request.META.get('HTTP_REFERER')    
    variant_id = request.POST.get('variant_id')
    cart_user = Cart.objects.get(user__id=request.user.id)
    cart_items = CartItem.objects.get(cart__id=cart_user, variant__id=variant_id)

    cart_items.delete()
    
    return HttpResponseRedirect(url)


def clear_cart(request):  
    url = request.META.get('HTTP_REFERER')
    cart_user = Cart.objects.get(user__id=request.user.id)
    cart_user.delete()

    return HttpResponseRedirect(url)
    



    
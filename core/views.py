from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from  django.views.generic import ListView, DetailView, View
from django.shortcuts import render, redirect, get_object_or_404
from .models import Item, OrderItem, Order

# home page view
def acceuil(request):
    items = Item.objects.all()
    # order_item, created = OrderItem.objects.get_or_create(
    #     item=item,
    #     user=request.user,
    #     ordered=False
    # )
    context = {
        'items':items,  
    }
    orders = Order.objects.filter(user=request.user, ordered=False)
    if orders.exists():
        order = orders[0]
        context['order'] = order

    return render(request, 'core/index.html', context)

def product_detail(request, id):
    
    item = Item.objects.get(id=id)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
    context = {
        'order_item':order_item,
        'item':item,
    }

    orders = Order.objects.filter(user=request.user, ordered=False)
    if orders.exists():
        order = orders[0]
        context['order'] = order
    
    return render(request, 'core/product-detail.html', context)





@login_required
def add_to_cart(request, id):
    """ add to cart view method manager """
    #get of the item
    item = get_object_or_404(Item, id=id)
    #geting of the order_item, or creation if not exists
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
    #get of the order of the current user, and (not ordered)
    order_queryset = Order.objects.filter(user=request.user, ordered=False)
    #case: if the user has alrady an unordered order
    if order_queryset.exists():
        #get of the order in the query set
        order = order_queryset[0]
        #check if the order item is in the order
        if order.items.filter(id=order_item.id).exists():
            #don't do nothing
            if len(order_item.item.title.strip()) > 15:
                item_title = order_item.item.title.strip()
            else:
                item_title = order_item.item.title.strip()
            messages.info(request, f'Le produit {item_title} a ete deja ajouter dans le panier.')
        #the item not in the cart
        else:
            if len(order_item.item.title.strip()) > 15:
                item_title = order_item.item.title.strip()
            else:
                item_title = order_item.item.title.strip()
            messages.info(request, f'Le produit {item_title} a ete deja ajouter dans le panier.')
            #add in the cart
            order.items.add(order_item)
    else:
        #the user has not alrady an unordered order
        ordered_date = timezone.now()
        #creation of a new order
        order = Order.objects.create(
            user=request.user, ordered_date=ordered_date
        )
        #adding the current item to add in the cart
        if len(order_item.item.title.strip()) > 15:
                item_title = order_item.item.title.strip()
        else:
            item_title = order_item.item.title.strip()
        order.items.add(order_item)
        messages.info(request, f'Le produit {item_title} a ete deja ajouter dans le panier.')

    return redirect('core:product', id=id)


@login_required
def remove_from_cart(request, id):
    """ Remove item view """
    item = get_object_or_404(Item, id=id)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )

    order_queryset = Order.objects.filter(user=request.user, ordered=False)
    #check if the orderqs exists
    if order_queryset.exists():
        order = order_queryset[0]
        #check if the order item is in the order
        if order.items.filter(id=order_item.id).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order.items.remove(order_item)
            order_item.delete()
            messages.info(request, f'Le produit a ete supprimer du panier.')
        else:
            messages.info(request, 'Le produit n\'est pas ete ajouter dans le panier')
            return redirect('core:product', id=id)
    else:
        messages.info(request, '..........')
    return redirect('core:product', id=id)

#order summary
class OrderSummaryView(LoginRequiredMixin, View):
    """ Order summary page view """
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
        except ObjectDoesNotExist:
            messages.error(self.request, "You don't have an Order")
            return redirect('/')
        context = {'order':order}
        return render(self.request, 'core/cart.html', context)

from django import template
from core.models import Order, OrderItem

register = template.Library()

@register.filter
def cart_item_count(user):
    if user.is_authenticated:
        orderqs = Order.objects.filter(user=user, ordered=False)
        if orderqs.exists():
            return orderqs[0].items.count()
    return 0

# @register.filter
# def carts(user):
#      order = Order.objects.filter(user=request.user, ordered=False)
#      context = {'order':order}
#      return order


    
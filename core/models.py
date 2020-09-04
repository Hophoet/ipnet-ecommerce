from django.db import models
from django.conf import settings
from django.shortcuts import reverse


#Set of the item categories
CATEGORY_CHOICES = (
    ('C', 'Chaussure'),
    ('TS', 'Tee Shirt'),
    ('P', 'Pantalon'),
    ('M', 'Montre'),
    ('S', 'Sac'),
)

#Set of the items labels
LABEL_CHOICES = (
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger'),
)

class Item(models.Model):
    """ product item model class """
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(null=True, blank=True)
    image = models.ImageField(upload_to='images/items', null=True, blank=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1)
    description = models.TextField()
    quantity = models.IntegerField(default=1)


    def __str__(self):
        return self.title

    def get_save_price(self):
        if self.discount_price:
            return self.price - self.discount_price

    def get_save_price_pourcentage(self):
        if self.discount_price:
            return int( ( self.get_save_price() * 100 )/self.price )
    # def get_absolute_url(self):
    #     return reverse('core:product', kwargs={
    #         'slug':self.id
    #     })

    # def get_add_to_cart_url(self):
    #     """ add to cart url getter """
    #     #redirection to the product detail view page
    #     return reverse('core:add-to-cart', kwargs={
    #         'slug':self.slug
    #     })
    # def get_remove_from_cart_url(self):
    #     """ remove from cart url getter """
    #     #redirection to the product detail view page
    #     return reverse('core:remove-from-cart', kwargs={
    #         'slug':self.slug
    #     })

class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.quantity} of {self.item.title}'

    #total item price getter
    def get_total_item_price(self):
        """Total item price getter """
        return self.item.price * self.quantity

    #total disount item price getter
    def get_total_discount_item_price(self):
        """Total discount item price getter """
        return self.item.discount_price * self.quantity

    #total saved ammount getter
    def get_amount_saved(self):
        """ Total saved ammount getter """
        return self.get_total_item_price() - self.get_total_discount_item_price()

    #finale price getter
    def get_final_price(self):
        """finale price getter """
        if self.item.discount_price:
            return self.get_total_discount_item_price()
        return self.get_total_item_price()



#coupon model
class Coupon(models.Model):
    code = models.CharField(max_length=30)
    amount = models.FloatField()

    def __str__(self):
        """ Coupon instance print method """
        return self.code


#Order model
class Order(models.Model):
    """ order actions model class """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ref_code = models.CharField(max_length=20)
    items = models.ManyToManyField(OrderItem)
    coupon = models.ForeignKey(Coupon, on_delete=models.SET_NULL, blank=True, null=True)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    being_delivered = models.BooleanField(default=False)

    def get_total_price(self):
        total_price = 0
        for  order_item in  self.items.all():
            total_price += order_item.get_final_price()

        return total_price

  

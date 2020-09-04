
#from django.config.urls import url
from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.acceuil, name='home'),
    path('product/<int:id>/', views.product_detail, name='product'),
    path('add-to-cart/<int:id>', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.OrderSummaryView.as_view(), name='cart'),

    path('remove-from-cart/<int:id>', views.remove_from_cart, name='remove_from_cart'),

]
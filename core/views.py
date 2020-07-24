from django.shortcuts import render
from .models import Item

# home page view
def acceuil(request):
    items = Item.objects.all()
    context = {'items':items}
    return render(request, 'core/index.html', context)
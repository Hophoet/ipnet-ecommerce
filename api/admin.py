from django.contrib import admin
from .models import Produit, Categorie, Fournisseur, Images
# Register your models here.

admin.site.register(Produit)
admin.site.register(Fournisseur)
admin.site.register(Categorie)
admin.site.register(Images)
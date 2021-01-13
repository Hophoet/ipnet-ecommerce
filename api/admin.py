from django.contrib import admin
from .models import (Produit, Categorie, Fournisseur, Image,
ProduitACommander, Panier)
# Register your models here.

admin.site.register(Produit)
admin.site.register(Fournisseur)
admin.site.register(Categorie)
admin.site.register(Image)
admin.site.register(Panier)
admin.site.register(ProduitACommander)

from django.urls import path

from . import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('categories/', views.listeCategories, name="categories"),
    path('categorie-enregistrer/', views.enregistrerCategorie, name="enregistrer_categorie"),
    path('categorie/detail/<int:id>', views.detailCategorie, name="detail_categorie"),

    path('produits/', views.listeProduits, name="produits"),
    path('produit-enregistrer/', views.enregistrerProduit, name="enregistrer_produit"),
    path('produit/detail/<int:id>', views.detailProduit, name="detail_produit"),
    
    path('images/', views.listeImages, name="images"),
    path('image/detail/<int:id>', views.detailImage, name="detail_image"),
]

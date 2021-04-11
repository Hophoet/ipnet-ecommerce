from django.urls import path, include
from knox import views as knox_views

from . import(views, gestion_categorie, gestion_produit, 
                gestion_fournisseur, gestion_utilisateur, gestion_panier,
                gestion_image, gestion_user)

urlpatterns = [
    #path('categories/', views.CategoriesListe().as_view(), name='categories'),
    #path('fournisseurs/', views.FournisseursListe().as_view(), name='fournisseurs'),
    #path('commandes/', views.UtilisateurCommandesListe().as_view(), name='commandes'),
    #path('ajout-au-panier/<int:produit_id>/',
    #     views.AjoutAuPanierView().as_view(), name='ajout_au_panier'),
    #path('commander/', views.CommanderView().as_view(), name='commander'),

    path('auth/', include('knox.urls')),
    path('auth/registrer/', gestion_user.RegisterUserApi.as_view(), name="knox_register"),
    path('auth/connecter/', gestion_user.LoginUserApi.as_view(), name="knox_login"),
    path('auth/user/', gestion_user.UserReturnApi.as_view(), name="knox_user"),
    path('auth/logout/', knox_views.LogoutView.as_view(), name='knox_logout'),


    path('ajout-categorie/', gestion_categorie.ajoutCategorie, name='ajout_categorie'),
    path('categorie/<int:id>/', gestion_categorie.categorie, name='categorie'),
    path('categories/', gestion_categorie.categories, name='categories'),


    path('ajout-fournisseur/', gestion_fournisseur.ajoutFournisseur, name='ajout_fournisseur'),
    path('fournisseur/<int:id>/', gestion_fournisseur.fournisseur, name='fournisseur'),
    path('fournisseurs/', gestion_fournisseur.fournisseurs, name='fournisseurs'),



    path('ajout-produit/', gestion_produit.ajoutProduit, name='ajout_produit'),
    path('produits/', gestion_produit.produits, name='liste_produit'),
    path('produit/<int:id>/', gestion_produit.produit, name='produit'),


    path('ajout-utilisateur/', gestion_utilisateur.ajoutUtilisateur, name='ajout_utilisateur'),
    path('utilisateur/<int:id>/', gestion_utilisateur.utilisateur, name='utilisateur'),


    path('ajout-panier/', gestion_panier.ajoutPanier, name='ajout_panier'),
    path('panier/<int:id>/', gestion_panier.panier, name='panier'),

    path('ajouter-au-panier/<int:id>/<int:quantite>/', gestion_panier.ajouterAuPanier, name='ajouter_au_panier'),


    path('upload/', gestion_image.FileUploadView.as_view()),
    path('images-produit/<int:id>/', gestion_image.images_produit, name="images"),
    path('image-produit/<int:id>/', gestion_image.image_produit, name="image"),



    
]

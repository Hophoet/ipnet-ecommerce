from django.urls import path
#from knox import views as knox_views

from . import(views, gestion_categorie, gestion_produit, gestion_fournisseur, gestion_utilisateur, gestion_panier)

urlpatterns = [
    #path('categories/', views.CategoriesListe().as_view(), name='categories'),
    #path('fournisseurs/', views.FournisseursListe().as_view(), name='fournisseurs'),
    #path('commandes/', views.UtilisateurCommandesListe().as_view(), name='commandes'),
    #path('ajout-au-panier/<int:produit_id>/',
    #     views.AjoutAuPanierView().as_view(), name='ajout_au_panier'),
    #path('commander/', views.CommanderView().as_view(), name='commander'),

    #path('auth/', include('knox.urls))
    #path('auth/logout', knox_views.LogoutView.as_view(), name='knox_logout')


    path('ajout-categorie/', gestion_categorie.ajoutCategorie, name='ajout_categorie'),
    path('categorie/', gestion_categorie.categorie, name='categorie'),


    path('ajout-fournisseur/', gestion_fournisseur.ajoutFournisseur, name='ajout_fournisseur'),
    path('fournisseur/', gestion_fournisseur.fournisseur, name='fournisseur'),



    path('ajout-produit/', gestion_produit.ajoutProduit, name='ajout_produit'),
    path('produits/', gestion_produit.produits, name='liste_produit'),
    path('produit/<int:id>/', gestion_produit.produit, name='produit'),


    path('ajout-utilisateur/', gestion_utilisateur.ajoutUtilisateur, name='ajout_utilisateur'),
    path('utilisateur/<int:id>/', gestion_utilisateur.utilisateur, name='utilisateur'),


    path('ajout-panier/', gestion_panier.ajoutPanier, name='ajout_panier'),
    path('panier/<int:id>/', gestion_panier.panier, name='panier'),

    path('ajouter-au-panier/<int:id>/<int:quantite>/', gestion_panier.ajouterAuPanier, name='ajouter_au_panier'),
]

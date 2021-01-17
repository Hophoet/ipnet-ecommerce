from django.urls import path

from . import views
urlpatterns = [
    path('categories/', views.CategoriesListe().as_view(), name='categories'),
    path('fournisseurs/', views.FournisseursListe().as_view(), name='fournisseurs'),
    path('commandes/', views.UtilisateurCommandesListe().as_view(), name='commandes'),
]

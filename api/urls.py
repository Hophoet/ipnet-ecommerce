from django.urls import path

from . import views
urlpatterns = [
    path('categories/', views.CategoriesListe().as_view(), name='categories')
]

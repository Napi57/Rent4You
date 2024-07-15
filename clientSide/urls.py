from django.urls import path
from . import views




urlpatterns = [
    path('accueil/', views.page_accueil,name='accueil'),
    path('search/', views.search, name='search'),
    path('offre/<pk>', views.offre, name='offre'),
    path('signature/', views.signature, name='signature'),

    path('register/',views.register_form, name='register'),
    path('login/', views.login_locataire, name='login'),
    path('logout/', views.logouts, name='logout'),
    path('historique/<id>', views.historique_réservation, name='historique'),
    path('profile/<id>', views.profile, name='profile'),
    path('filter_price/<Lieu>', views.filter_price, name='filter_price'),
    path('conf/<loc>,<véh>,<dd>,<df>,<prix>', views.reservation, name='conf'),

    path('reservation/', views.reserv, name='reservation'),

]
from django.urls import path
from . import views

from django.urls import path
from .views import (
    FurnizorListCreateAPIView,
    FurnizorRetrieveUpdateDestroyAPIView,
    ContactListCreateAPIView,
    ContactRetrieveUpdateDestroyAPIView,
    ContactFurnizorListCreateAPIView,
    ContactFurnizorRetrieveUpdateDestroyAPIView,
    FacturaAchizitieListCreateAPIView,
    FacturaAchizitieRetrieveUpdateDestroyAPIView,
    ProdusListCreateAPIView,
    ProdusRetrieveUpdateDestroyAPIView,
    ReceptieMarfaListCreateAPIView,
    ReceptieMarfaRetrieveUpdateDestroyAPIView,
    ProduseReceptionateListCreateAPIView,
    ProduseReceptionateRetrieveUpdateDestroyAPIView,
)


urlpatterns = [
    path('', views.index, name='index'),

    path('furnizori', views.index_furnizor, name='index_furnizori'),
    path('furnizori/<int:id>', views.vezi_furnizor, name='vezi_furnizor'),
    path('furnizori/adauga/', views.adauga_furnizor, name='adauga_furnizor'),
    path('furnizori/editeaza/<int:id>',
         views.editeaza_furnizor, name='editeaza_furnizor'),
    path('furnizori/sterge/<int:id>',
         views.sterge_furnizor, name='sterge_furnizor'),



    path('contacte', views.index_contacte, name='index_contacte'),
    path('contacte/<int:id>', views.vezi_contact, name='vezi_contact'),
    path('contacte/adauga/', views.adauga_contact, name='adauga_contact'),
    path('contacte/editeaza/<int:id>',
         views.editeaza_contact, name='editeaza_contact'),
    path('contacte/sterge/<int:id>',
         views.sterge_contact, name='sterge_contact'),



    path('drf/furnizori/', FurnizorListCreateAPIView.as_view(), name='furnizor'),
    path('drf/furnizor/<int:id>/',
         FurnizorRetrieveUpdateDestroyAPIView.as_view(), name='furnizor_id'),


    path('drf/contacte/', ContactListCreateAPIView.as_view(), name='Contact'),
    path('drf/contacte/<int:id>/',
         ContactRetrieveUpdateDestroyAPIView.as_view(), name='Contact_id'),


    path('drf/contacte_furnizor/',
         ContactFurnizorListCreateAPIView.as_view(), name='ContactFurnizor'),
    path('drf/contacte_furnizor/<int:id>/',
         ContactFurnizorRetrieveUpdateDestroyAPIView.as_view(), name='ContactFurnizor_id'),


    path('drf/facturi_achizitie/',
         FacturaAchizitieListCreateAPIView.as_view(), name='FacturaAchizitie'),
    path('drf/facturi_achizitie/<int:id>/',
         FacturaAchizitieRetrieveUpdateDestroyAPIView.as_view(), name='FacturaAchizitie_id'),


    path('drf/produse/', ProdusListCreateAPIView.as_view(), name='Produs'),
    path('drf/produse/<int:id>/',
         ProdusRetrieveUpdateDestroyAPIView.as_view(), name='Produs_id'),


    path('drf/receptie_marfa/', ReceptieMarfaListCreateAPIView.as_view(),
         name='ReceptieMarfa'),
    path('drf/receptie_marfa/<int:id>/',
         ReceptieMarfaRetrieveUpdateDestroyAPIView.as_view(), name='ReceptieMarfa_id'),


    path('drf/produse_receptionate/',
         ProduseReceptionateListCreateAPIView.as_view(), name='ProduseReceptionate'),
    path('drf/produse_receptionate/<int:id>/',
         ProduseReceptionateRetrieveUpdateDestroyAPIView.as_view(), name='ProduseReceptionate_id'),

]

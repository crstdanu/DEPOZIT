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

    path('furnizor/', views.index_furnizor, name='index_furnizor'),
    path('furnizor/<int:id>', views.vezi_furnizor, name='vezi_furnizor'),
    path('furnizor/adauga/', views.adauga_furnizor, name='adauga_furnizor'),
    path('furnizor/editeaza/<int:id>',
         views.editeaza_furnizor, name='editeaza_furnizor'),
    path('furnizor/sterge/<int:id>', views.sterge_furnizor, name='sterge_furnizor'),



    path('drf/furnizor/', FurnizorListCreateAPIView.as_view(), name='furnizor'),
    path('drf/furnizor/<int:id>/',
         FurnizorRetrieveUpdateDestroyAPIView.as_view(), name='furnizor_id'),


    path('drf/contact/', ContactListCreateAPIView.as_view(), name='Contact'),
    path('drf/contact/<int:id>/',
         ContactRetrieveUpdateDestroyAPIView.as_view(), name='Contact_id'),


    path('drf/contactfurnizor/',
         ContactFurnizorListCreateAPIView.as_view(), name='ContactFurnizor'),
    path('drf/contactfurnizor/<int:id>/',
         ContactFurnizorRetrieveUpdateDestroyAPIView.as_view(), name='ContactFurnizor_id'),


    path('drf/facturaachizitie/',
         FacturaAchizitieListCreateAPIView.as_view(), name='FacturaAchizitie'),
    path('drf/facturaachizitie/<int:id>/',
         FacturaAchizitieRetrieveUpdateDestroyAPIView.as_view(), name='FacturaAchizitie_id'),


    path('drf/produs/', ProdusListCreateAPIView.as_view(), name='Produs'),
    path('drf/produs/<int:id>/',
         ProdusRetrieveUpdateDestroyAPIView.as_view(), name='Produs_id'),


    path('drf/receptiemarfa/', ReceptieMarfaListCreateAPIView.as_view(),
         name='ReceptieMarfa'),
    path('drf/receptiemarfa/<int:id>/',
         ReceptieMarfaRetrieveUpdateDestroyAPIView.as_view(), name='ReceptieMarfa_id'),


    path('drf/produsereceptionate/',
         ProduseReceptionateListCreateAPIView.as_view(), name='ProduseReceptionate'),
    path('drf/produsereceptionate/<int:id>/',
         ProduseReceptionateRetrieveUpdateDestroyAPIView.as_view(), name='ProduseReceptionate_id'),

]

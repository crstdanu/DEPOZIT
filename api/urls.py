from django.urls import path
from .views import *


urlpatterns = [
    path('furnizor/', FurnizorListCreateAPIView.as_view(), name='furnizor'),
    path('furnizor/<int:id>/',
         FurnizorRetrieveUpdateDestroyAPIView.as_view(), name='furnizor_id'),

    path('contact/', ContactListCreateAPIView.as_view(), name='Contact'),
    path('contact/<int:id>/',
         ContactRetrieveUpdateDestroyAPIView.as_view(), name='Contact_id'),

    path('contactfurnizor/', ContactFurnizorListCreateAPIView.as_view(),
         name='ContactFurnizor'),
    path('contactfurnizor/<int:id>/',
         ContactFurnizorRetrieveUpdateDestroyAPIView.as_view(), name='ContactFurnizor_id'),

    path('facturaachizitie/', FacturaAchizitieListCreateAPIView.as_view(),
         name='FacturaAchizitie'),
    path('facturaachizitie/<int:id>/',
         FacturaAchizitieRetrieveUpdateDestroyAPIView.as_view(), name='FacturaAchizitie_id'),

    path('produs/', ProdusListCreateAPIView.as_view(), name='Produs'),
    path('produs/<int:id>/',
         ProdusRetrieveUpdateDestroyAPIView.as_view(), name='Produs_id'),

    path('receptiemarfa/', ReceptieMarfaListCreateAPIView.as_view(),
         name='ReceptieMarfa'),
    path('receptiemarfa/<int:id>/',
         ReceptieMarfaRetrieveUpdateDestroyAPIView.as_view(), name='ReceptieMarfa_id'),

    path('produsereceptionate/', ProduseReceptionateListCreateAPIView.as_view(),
         name='ProduseReceptionate'),
    path('produsereceptionate/<int:id>/',
         ProduseReceptionateRetrieveUpdateDestroyAPIView.as_view(), name='ProduseReceptionate_id'),
]

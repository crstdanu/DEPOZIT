from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from Gestiune.models import *
from .serializers import *


class FurnizorListCreateAPIView(ListCreateAPIView):
    queryset = Furnizor.objects.all()
    serializer_class = FurnizorSerializer


class FurnizorRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Furnizor.objects.all()
    serializer_class = FurnizorSerializer
    lookup_field = 'id'


#
class ContactListCreateAPIView(ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    lookup_field = 'id'

#


class ContactFurnizorListCreateAPIView(ListCreateAPIView):
    queryset = ContactFurnizor.objects.all()
    serializer_class = ContactFurnizorSerializer


class ContactFurnizorRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ContactFurnizor.objects.all()
    serializer_class = ContactFurnizorSerializer
    lookup_field = 'id'

#


class FacturaAchizitieListCreateAPIView(ListCreateAPIView):
    queryset = FacturaAchizitie.objects.all()
    serializer_class = FacturaAchizitieSerializer


class FacturaAchizitieRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = FacturaAchizitie.objects.all()
    serializer_class = FacturaAchizitieSerializer
    lookup_field = 'id'

#


class ProdusListCreateAPIView(ListCreateAPIView):
    queryset = Produs.objects.all()
    serializer_class = ProdusSerializer


class ProdusRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Produs.objects.all()
    serializer_class = ProdusSerializer
    lookup_field = 'id'


#
class ReceptieMarfaListCreateAPIView(ListCreateAPIView):
    queryset = ReceptieMarfa.objects.all()
    serializer_class = ReceptieMarfaSerializer


class ReceptieMarfaRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ReceptieMarfa.objects.all()
    serializer_class = ReceptieMarfaSerializer
    lookup_field = 'id'

#


class ProduseReceptionateListCreateAPIView(ListCreateAPIView):
    queryset = ProduseReceptionate.objects.all()
    serializer_class = ProduseReceptionateSerializer


class ProduseReceptionateRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ProduseReceptionate.objects.all()
    serializer_class = ProduseReceptionateSerializer
    lookup_field = 'id'

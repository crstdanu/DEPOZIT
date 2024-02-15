from rest_framework.serializers import ModelSerializer
from Gestiune.models import (
    Furnizor,
    Contact,
    ContactFurnizor,
    FacturaAchizitie,
    Produs,
    ReceptieMarfa,
    ProduseReceptionate
)


class FurnizorSerializer(ModelSerializer):
    class Meta:
        model = Furnizor
        fields = '__all__'


class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class ContactFurnizorSerializer(ModelSerializer):
    class Meta:
        model = ContactFurnizor
        fields = '__all__'


class FacturaAchizitieSerializer(ModelSerializer):
    class Meta:
        model = FacturaAchizitie
        fields = '__all__'


class ProdusSerializer(ModelSerializer):
    class Meta:
        model = Produs
        fields = '__all__'


class ReceptieMarfaSerializer(ModelSerializer):
    class Meta:
        model = ReceptieMarfa
        fields = '__all__'


class ProduseReceptionateSerializer(ModelSerializer):
    class Meta:
        model = ProduseReceptionate
        fields = '__all__'

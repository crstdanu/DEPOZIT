from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import (
    Furnizor,
    Contact,
    ContactFurnizor,
    FacturaAchizitie,
    Produs,
    ReceptieMarfa,
    ProduseReceptionate,
)

from .forms import FurnizorForm

from .serializers import (
    FurnizorSerializer,
    ContactSerializer,
    ContactFurnizorSerializer,
    FacturaAchizitieSerializer,
    ProdusSerializer,
    ReceptieMarfaSerializer,
    ProduseReceptionateSerializer,
)

# Create your views here.
def index(request):
    return render(request, 'Gestiune/index.html')

def index_furnizor(request):
    return render(request, 'Gestiune/furnizor/index.html', {'furnizori': Furnizor.objects.all()})


def vezi_furnizor(request, id):
    return HttpResponseRedirect(reverse('index_furnizor'))


def adauga_furnizor(request):
    if request.method == 'POST':
        form = FurnizorForm(request.POST)
        if form.is_valid():
            new_cui = form.cleaned_data['cui']
            new_nume = form.cleaned_data['nume']
            new_adresa = form.cleaned_data['adresa']
            new_numar_reg_com = form.cleaned_data['numar_reg_com']
            new_telefon = form.cleaned_data['telefon']

            new_furnizor = Furnizor(
                cui=new_cui,
                nume=new_nume,
                adresa=new_adresa,
                numar_reg_com=new_numar_reg_com,
                telefon=new_telefon,
            )
            new_furnizor.save()
            return render(request, 'Gestiune/furnizor/adauga.html', {
                'form': FurnizorForm(),
                'success': True
            })
    else:
        form = FurnizorForm()
    return render(request, 'Gestiune/furnizor/adauga.html', {
        'form': FurnizorForm()
    })


def editeaza_furnizor(request, id):
    if request.method == 'POST':
        furnizor = Furnizor.objects.get(pk=id)
        form = FurnizorForm(request.POST, instance=furnizor)
        if form.is_valid():
            form.save()
            return render(request, 'Gestiune/furnizor/editeaza.html', {
                'form': form,
                'success': True
            })
    else:
        student = Furnizor.objects.get(pk=id)
        form = FurnizorForm(instance=student)
    return render(request, 'Gestiune/furnizor/editeaza.html', {
        'form': form
    })


def sterge_furnizor(request, id):
    if request.method == 'POST':
        furnizor = Furnizor.objects.get(pk=id)
        furnizor.delete()
    return HttpResponseRedirect(reverse('index_furnizor'))


# def vezi_furnizor(request, id):
#     return HttpResponseRedirect(reverse('index'))


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

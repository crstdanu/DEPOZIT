from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from .models import (
    Furnizor,
    Contact,
    ContactFurnizor,
    FacturaAchizitie,
    Produs,
    ReceptieMarfa,
    ProduseReceptionate,
)

from .forms import FurnizorForm, ContactForm

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
    return render(request, 'Gestiune/furnizori/index.html', {'furnizori': Furnizor.objects.all()})


def vezi_furnizor(request, id):
    return HttpResponseRedirect(reverse('index_furnizori'))


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
            return render(request, 'Gestiune/furnizori/adauga.html', {
                'form': FurnizorForm(),
                'success': True
            })
    else:
        form = FurnizorForm()
    return render(request, 'Gestiune/furnizori/adauga.html', {
        'form': FurnizorForm()
    })


def editeaza_furnizor(request, id):
    if request.method == 'POST':
        furnizor = Furnizor.objects.get(pk=id)
        form = FurnizorForm(request.POST, instance=furnizor)
        if form.is_valid():
            form.save()
            return render(request, 'Gestiune/furnizori/editeaza.html', {
                'form': form,
                'success': True
            })
    else:
        furnizor = Furnizor.objects.get(pk=id)
        form = FurnizorForm(instance=furnizor)
    return render(request, 'Gestiune/furnizori/editeaza.html', {
        'form': form
    })


def sterge_furnizor(request, id):
    if request.method == 'POST':
        furnizor = Furnizor.objects.get(pk=id)
        furnizor.delete()
    return HttpResponseRedirect(reverse('index_furnizori'))


def index_contacte(request):
    return render(request, 'Gestiune/contacte/index.html', {'contacte': Contact.objects.all()})


def vezi_contact(request, id):
    return HttpResponseRedirect(reverse('index_contacte'))


def adauga_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            new_nume = form.cleaned_data['nume']
            new_nr_telefon = form.cleaned_data['nr_telefon']
            new_email = form.cleaned_data['email']

            new_contact = Furnizor(
                nume=new_nume,
                nr_telefon=new_nr_telefon,
                email=new_email,
            )
            new_contact.save()
            return render(request, 'Gestiune/contacte/adauga.html', {
                'form': FurnizorForm(),
                'success': True
            })
    else:
        form = ContactForm()
    return render(request, 'Gestiune/contacte/adauga.html', {
        'form': ContactForm()
    })


def editeaza_contact(request, id):
    if request.method == 'POST':
        contact = Contact.objects.get(pk=id)
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return render(request, 'Gestiune/contacte/editeaza.html', {
                'form': form,
                'success': True
            })
    else:
        contact = Contact.objects.get(pk=id)
        form = ContactForm(instance=contact)
    return render(request, 'Gestiune/contacte/editeaza.html', {
        'form': form
    })


def sterge_contact(request, id):
    if request.method == 'POST':
        contact = Contact.objects.get(pk=id)
        contact.delete()
    return HttpResponseRedirect(reverse('index_contacte'))


class FurnizorListCreateAPIView(ListCreateAPIView):
    queryset = Furnizor.objects.all()
    serializer_class = FurnizorSerializer
    # filter_backends = [filters.OrderingFilter]
    # filter_backends = [filters.SearchFilter]
    filterset_fields = ['cui', 'nume', 'adresa', 'numar_reg_com', 'telefon']


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

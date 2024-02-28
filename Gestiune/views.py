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

from .forms import FurnizorForm, ContactForm, ContactFurnizorForm, FacturaAchizitieForm, ProdusForm, ReceptieMarfaForm, ProduseReceptionateForm

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


# clasa Furnizor

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


# Clasa Contact


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

            new_contact = Contact(
                nume=new_nume,
                nr_telefon=new_nr_telefon,
                email=new_email,
            )
            new_contact.save()
            return render(request, 'Gestiune/contacte/adauga.html', {
                'form': ContactForm(),
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


# Clasa ContactFurnizori


def index_contacte_furnizori(request):
    return render(request, 'Gestiune/contacte_furnizori/index.html', {'contacte_furnizori': ContactFurnizor.objects.all()})


def vezi_contact_furnizor(request, id):
    return HttpResponseRedirect(reverse('index_contacte_furnizor'))


def adauga_contact_furnizor(request):
    if request.method == 'POST':
        form = ContactFurnizorForm(request.POST)
        if form.is_valid():
            new_furnizor = form.cleaned_data['furnizor']
            new_persoana_de_contact = form.cleaned_data['persoana_de_contact']

            new_contact_furnizor = ContactFurnizor(
                furnizor=new_furnizor,
                persoana_de_contact=new_persoana_de_contact,
            )
            new_contact_furnizor.save()
            return render(request, 'Gestiune/contacte_furnizori/adauga.html', {
                'form': ContactFurnizorForm(),
                'success': True
            })
    else:
        form = ContactFurnizorForm()
    return render(request, 'Gestiune/contacte_furnizori/adauga.html', {
        'form': ContactFurnizorForm()
    })


def editeaza_contact_furnizor(request, id):
    if request.method == 'POST':
        contact_furnizor = ContactFurnizor.objects.get(pk=id)
        form = ContactFurnizorForm(request.POST, instance=contact_furnizor)
        if form.is_valid():
            form.save()
            return render(request, 'Gestiune/contacte_furnizori/editeaza.html', {
                'form': form,
                'success': True
            })
    else:
        contact_furnizor = ContactFurnizor.objects.get(pk=id)
        form = ContactFurnizorForm(instance=contact_furnizor)
    return render(request, 'Gestiune/contacte_furnizori/editeaza.html', {
        'form': form
    })


def sterge_contact_furnizor(request, id):
    if request.method == 'POST':
        contact_furnizor = ContactFurnizor.objects.get(pk=id)
        contact_furnizor.delete()
    return HttpResponseRedirect(reverse('index_contacte_furnizori'))


# Clasa FacturaAchizitie


def index_facturi_achizitie(request):
    return render(request, 'Gestiune/facturi_achizitie/index.html', {'facturi_achizitie': FacturaAchizitie.objects.all()})


def vezi_factura_achizitie(request, id):
    return HttpResponseRedirect(reverse('index_facturi_achizitie'))


def adauga_factura_achizitie(request):
    if request.method == 'POST':
        form = FacturaAchizitieForm(request.POST)
        if form.is_valid():
            new_furnizor = form.cleaned_data['furnizor']
            new_nr_factura = form.cleaned_data['nr_factura']
            new_valoare_factura = form.cleaned_data['valoare_factura']

            new_factura_achizitie = FacturaAchizitie(
                furnizor=new_furnizor,
                nr_factura=new_nr_factura,
                valoare_factura=new_valoare_factura,
            )
            new_factura_achizitie.save()
            return render(request, 'Gestiune/facturi_achizitie/adauga.html', {
                'form': FacturaAchizitieForm(),
                'success': True
            })
    else:
        form = FacturaAchizitieForm()
    return render(request, 'Gestiune/facturi_achizitie/adauga.html', {
        'form': FacturaAchizitieForm()
    })


def editeaza_factura_achizitie(request, id):
    if request.method == 'POST':
        factura_achizitie = FacturaAchizitie.objects.get(pk=id)
        form = FacturaAchizitieForm(request.POST, instance=factura_achizitie)
        if form.is_valid():
            form.save()
            return render(request, 'Gestiune/facturi_achizitie/editeaza.html', {
                'form': form,
                'success': True
            })
    else:
        factura_achizitie = FacturaAchizitie.objects.get(pk=id)
        form = FacturaAchizitieForm(instance=factura_achizitie)
    return render(request, 'Gestiune/facturi_achizitie/editeaza.html', {
        'form': form
    })


def sterge_factura_achizitie(request, id):
    if request.method == 'POST':
        factura_achizitie = FacturaAchizitie.objects.get(pk=id)
        factura_achizitie.delete()
    return HttpResponseRedirect(reverse('index_facturi_achizitie'))


# Clasa Produs


def index_produse(request):
    return render(request, 'Gestiune/produse/index.html', {'produse': Produs.objects.all()})


def vezi_produse(request, id):
    return HttpResponseRedirect(reverse('index_produse'))


def adauga_produse(request):
    if request.method == 'POST':
        form = ProdusForm(request.POST)
        if form.is_valid():
            new_nume_produs = form.cleaned_data['nume_produs']
            new_ean = form.cleaned_data['ean']
            new_serial_number = form.cleaned_data['serial_number']
            new_producator = form.cleaned_data['producator']
            new_descriere = form.cleaned_data['descriere']
            new_cantitate_in_stoc = form.cleaned_data['cantitate_in_stoc']

            new_produs = Produs(
                nume_produs=new_nume_produs,
                ean=new_ean,
                serial_number=new_serial_number,
                producator=new_producator,
                descriere=new_descriere,
                cantitate_in_stoc=new_cantitate_in_stoc,
            )
            new_produs.save()
            return render(request, 'Gestiune/produse/adauga.html', {
                'form': ProdusForm(),
                'success': True
            })
    else:
        form = ProdusForm()
    return render(request, 'Gestiune/produse/adauga.html', {
        'form': ProdusForm()
    })


def editeaza_produse(request, id):
    if request.method == 'POST':
        produs = Produs.objects.get(pk=id)
        form = ProdusForm(request.POST, instance=produs)
        if form.is_valid():
            form.save()
            return render(request, 'Gestiune/produse/editeaza.html', {
                'form': form,
                'success': True
            })
    else:
        produs = Produs.objects.get(pk=id)
        form = ProdusForm(instance=produs)
    return render(request, 'Gestiune/produse/editeaza.html', {
        'form': form
    })


def sterge_produse(request, id):
    if request.method == 'POST':
        produs = Produs.objects.get(pk=id)
        produs.delete()
    return HttpResponseRedirect(reverse('index_produse'))


# Clasa ReceptieMarfa


def index_receptie_marfuri(request):
    return render(request, 'Gestiune/receptie_marfuri/index.html', {'receptie_marfuri': ReceptieMarfa.objects.all()})


def vezi_receptie_marfuri(request, id):
    return HttpResponseRedirect(reverse('index_receptie_marfuri'))


def adauga_receptie_marfuri(request):
    if request.method == 'POST':
        form = ReceptieMarfaForm(request.POST)
        if form.is_valid():
            new_furnizor = form.cleaned_data['furnizor']
            new_receptionat_de = form.cleaned_data['receptionat_de']

            new_receptie = ReceptieMarfa(
                furnizor=new_furnizor,
                receptionat_de=new_receptionat_de,
            )
            new_receptie.save()
            return render(request, 'Gestiune/receptie_marfuri/adauga.html', {
                'form': ReceptieMarfaForm(),
                'success': True
            })
    else:
        form = ReceptieMarfaForm()
    return render(request, 'Gestiune/receptie_marfuri/adauga.html', {
        'form': ReceptieMarfaForm()
    })


def editeaza_receptie_marfuri(request, id):
    if request.method == 'POST':
        receptie = ReceptieMarfa.objects.get(pk=id)
        form = ReceptieMarfaForm(request.POST, instance=receptie)
        if form.is_valid():
            form.save()
            return render(request, 'Gestiune/receptie_marfuri/editeaza.html', {
                'form': form,
                'success': True
            })
    else:
        receptie = ReceptieMarfa.objects.get(pk=id)
        form = ReceptieMarfaForm(instance=receptie)
    return render(request, 'Gestiune/receptie_marfuri/editeaza.html', {
        'form': form
    })


def sterge_receptie_marfuri(request, id):
    if request.method == 'POST':
        receptie = ReceptieMarfa.objects.get(pk=id)
        receptie.delete()
    return HttpResponseRedirect(reverse('index_receptie_marfuri'))


# Clasa ProduseReceptionate


def index_produse_receptionate(request):
    return render(request, 'Gestiune/produse_receptionate/index.html', {'produse_receptionate': ProduseReceptionate.objects.all()})


def vezi_produse_receptionate(request, id):
    return HttpResponseRedirect(reverse('index_produse_receptionate'))


def adauga_produse_receptionate(request):
    if request.method == 'POST':
        form = ProduseReceptionateForm(request.POST)
        if form.is_valid():
            new_receptie_marfa = form.cleaned_data['receptie_marfa']
            new_produs = form.cleaned_data['produs']
            new_cantitate = form.cleaned_data['cantitate']

            new_receptie_mf = ProduseReceptionate(
                receptie_marfa=new_receptie_marfa,
                produs=new_produs,
                cantitate=new_cantitate,
            )
            new_receptie_mf.save()
            return render(request, 'Gestiune/produse_receptionate/adauga.html', {
                'form': ProduseReceptionateForm(),
                'success': True
            })
    else:
        form = ProduseReceptionateForm()
    return render(request, 'Gestiune/produse_receptionate/adauga.html', {
        'form': ProduseReceptionateForm()
    })


def editeaza_produse_receptionate(request, id):
    if request.method == 'POST':
        receptie_mf = ProduseReceptionate.objects.get(pk=id)
        form = ProduseReceptionateForm(request.POST, instance=receptie_mf)
        if form.is_valid():
            form.save()
            return render(request, 'Gestiune/produse_receptionate/editeaza.html', {
                'form': form,
                'success': True
            })
    else:
        receptie_mf = ProduseReceptionate.objects.get(pk=id)
        form = ProduseReceptionateForm(instance=receptie_mf)
    return render(request, 'Gestiune/produse_receptionate/editeaza.html', {
        'form': form
    })


def sterge_produse_receptionate(request, id):
    if request.method == 'POST':
        receptie_mf = ProduseReceptionate.objects.get(pk=id)
        receptie_mf.delete()
    return HttpResponseRedirect(reverse('index_produse_receptionate'))


# REST API

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

from django import forms
from .models import Furnizor, Contact, ContactFurnizor, FacturaAchizitie, Produs, ReceptieMarfa, ProduseReceptionate


# Formular Furnizor

class FurnizorForm(forms.ModelForm):
    class Meta:
        model = Furnizor
        fields = ['cui', 'nume', 'adresa', 'numar_reg_com', 'telefon']
        labels = {
            'cui': 'C.U.I.',
            'nume': 'Nume',
            'adresa': 'Adresa',
            'numar_reg_com': 'Nr. Reg. Com.',
            'telefon': 'Telefon',
        }
        widgets = {
            'cui': forms.TextInput(attrs={'class': 'form-control'}),
            'nume': forms.TextInput(attrs={'class': 'form-control'}),
            'adresa': forms.TextInput(attrs={'class': 'form-control'}),
            'numar_reg_com': forms.TextInput(attrs={'class': 'form-control'}),
            'telefon': forms.TextInput(attrs={'class': 'form-control'}),
        }


# Formular Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['nume', 'nr_telefon', 'email']
        labels = {
            'nume': 'Nume',
            'nr_telefon': 'Telefon',
            'email': 'Email',
        }
        widgets = {
            'nume': forms.TextInput(attrs={'class': 'form-control'}),
            'nr_telefon': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }


# Formular ContactFurnizor

class ContactFurnizorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ContactFurnizorForm, self).__init__(*args, **kwargs)
        self.fields['furnizor'].queryset = Furnizor.objects.all()

    class Meta:
        model = ContactFurnizor
        fields = ['furnizor', 'persoana_de_contact']
        labels = {
            'furnizor': 'Furnizor',
            'persoana_de_contact': 'Persoană de contact'
        }
        widgets = {
            'furnizor': forms.Select(attrs={'class': 'form-control'}),
            'persoana_de_contact': forms.TextInput(attrs={'class': 'form-control'})
        }


# Formular FacturaAchizitie

class FacturaAchizitieForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FacturaAchizitieForm, self).__init__(*args, **kwargs)
        self.fields['furnizor'].queryset = Furnizor.objects.all()

    class Meta:
        model = FacturaAchizitie
        fields = ['furnizor', 'nr_factura', 'valoare_factura',]
        labels = {
            'furnizor': 'Furnizor',
            'nr_factura': 'Nr. factură',
            'valoare_factura': 'Valoare factură',
        }
        widgets = {
            'furnizor': forms.Select(attrs={'class': 'form-control'}),
            'nr_factura': forms.TextInput(attrs={'class': 'form-control'}),
            'valoare_factura': forms.TextInput(attrs={'class': 'form-control'}),
        }


# Formular Produs

class ProdusForm(forms.ModelForm):
    class Meta:
        model = Produs
        fields = ['nume_produs', 'ean', 'serial_number',
                  'producator', 'descriere', 'cantitate_in_stoc']
        labels = {
            'nume_produs': 'Nume produs',
            'ean': 'EAN',
            'serial_number': 'Serial',
            'producator': 'Producator',
            'descriere': 'Descriere',
            'cantitate_in_stoc': 'Cantitate in stoc',
        }
        widgets = {
            'nume_produs': forms.TextInput(attrs={'class': 'form-control'}),
            'ean': forms.TextInput(attrs={'class': 'form-control'}),
            'serial_number': forms.TextInput(attrs={'class': 'form-control'}),
            'producator': forms.TextInput(attrs={'class': 'form-control'}),
            'descriere': forms.TextInput(attrs={'class': 'form-control'}),
            'cantitate_in_stoc': forms.TextInput(attrs={'class': 'form-control'}),
        }


# Formular ReceptieMarfa

class ReceptieMarfaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ReceptieMarfaForm, self).__init__(*args, **kwargs)
        self.fields['furnizor'].queryset = Furnizor.objects.all()

    class Meta:
        model = ReceptieMarfa
        fields = ['furnizor', 'receptionat_de', ]
        labels = {
            'furnizor': 'Furnizor',
            'receptionat_de': 'Recepționat de',
        }
        widgets = {
            'furnizor': forms.Select(attrs={'class': 'form-control'}),
            'receptionat_de': forms.TextInput(attrs={'class': 'form-control'}),
        }


# Formular ReceptieMarfa

class ProduseReceptionateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProduseReceptionateForm, self).__init__(*args, **kwargs)
        self.fields['produs'].queryset = Produs.objects.all()

    class Meta:
        model = ProduseReceptionate
        fields = ['receptie_marfa', 'produs', 'cantitate']
        labels = {
            'receptie_marfa': 'Furnizor',
            'produs': 'Produs',
            'cantitate': 'Cantitate',
        }
        widgets = {
            'produs': forms.Select(attrs={'class': 'form-control'}),
            'receptie_marfa': forms.TextInput(attrs={'class': 'form-control'}),
            'cantitate': forms.TextInput(attrs={'class': 'form-control'}),
        }

from django import forms
from .models import Furnizor, Contact


class FurnizorForm(forms.ModelForm):
    class Meta:
        model = Furnizor
        fields = ['cui', 'nume', 'adresa', 'numar_reg_com', 'telefon']
        labels = {
            'cui': 'CUI',
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

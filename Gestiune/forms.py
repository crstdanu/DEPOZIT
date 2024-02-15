from django import forms
from .models import Furnizor


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

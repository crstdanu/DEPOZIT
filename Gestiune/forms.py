from django import forms
from .models import Furnizor, Contact, ContactFurnizor


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


# class ContactFurnizorForm(forms.ModelForm):
#     class Meta:
#         model = ContactFurnizor
#         fields = ['furnizor', 'persoana_de_contact']
#         labels = {
#             'furnizor': 'Furnizor',
#             'persoana_de_contact': 'Persoana de contact'
#         }
#         widgets = {
#             'furnizor': forms.TextInput(attrs={'class': 'form-control'}),
#             'persoana_de_contact': forms.TextInput(attrs={'class': 'form-control'})
#         }


class ContactFurnizorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ContactFurnizorForm, self).__init__(*args, **kwargs)
        self.fields['furnizor'].queryset = Furnizor.objects.all()

    class Meta:
        model = ContactFurnizor
        fields = ['furnizor', 'persoana_de_contact']
        labels = {
            'furnizor': 'Furnizor',
            'persoana_de_contact': 'Persoana de contact'
        }
        widgets = {
            'furnizor': forms.Select(attrs={'class': 'form-control'}),
            'persoana_de_contact': forms.TextInput(attrs={'class': 'form-control'})
        }

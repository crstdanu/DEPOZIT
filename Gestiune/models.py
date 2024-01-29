
from phonenumber_field.modelfields import PhoneNumberField
from address.models import AddressField
from django.db import models


class Furnizor(models.Model):
    class Meta:
        verbose_name_plural = 'Furnizori'

    nume = models.CharField(max_length=50)
    adresa = models.CharField(max_length=255)
    # ce ar trebui introdus la "categorie"? de servicii? de materii prime? in genul asta?
    categorie = models.CharField(max_length=255)
    companie = models.CharField(max_length=255)
    cui = models.CharField(max_length=9)  # cat de specific sa fiu aici?

    def __str__(self):
        return f'{self.nume}'


class Contact(models.Model):
    class Meta:
        verbose_name_plural = 'Contacte'

    nume = models.CharField(max_length=50)
    nr_telefon = PhoneNumberField(null=True, default=None)
    email = models.EmailField()

    def __str__(self):
        return f'{self.nume}'


class ContactFurnizor(models.Model):
    class Meta:
        verbose_name_plural = 'Contact Furnizori'

    furnizor = models.ForeignKey(Furnizor, on_delete=models.CASCADE)
    persoana_de_contact = models.CharField(max_length=255)

    def __str__(self):
        return f'Firma: {self.furnizor}, contact: {self.persoana_de_contact}'


class FacturaAchizitie(models.Model):
    class Meta:
        verbose_name_plural = 'Facturi Achizitie'

    furnizor = models.ForeignKey(ContactFurnizor, on_delete=models.CASCADE)
    nr_factura = models.BigIntegerField()  # trebuie sa fiu mai specific aici?


class Produs(models.Model):
    class Meta:
        verbose_name_plural = 'Produse'

    nume_produs = models.CharField(max_length=55)
    # cat de specific sa fiu aici?
    ean = models.BigIntegerField()
    # cat de specific sa fiu aici?
    serial_number = models.BigIntegerField()
    producator = models.CharField(max_length=50)
    descriere = models.CharField(max_length=255)
    creat_la = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nume_produs}'


class ReceptieMarfa(models.Model):
    class Meta:
        verbose_name_plural = 'Receptie Marfuri'

    furnizor = models.ForeignKey(ContactFurnizor, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    receptionat_de = models.CharField(max_length=50)


class ProduseReceptionate(models.Model):
    class Meta:
        verbose_name_plural = 'Produse Receptionate'

    receptie_marfa = models.CharField(max_length=2550)
    produs = models.ForeignKey(Produs, on_delete=models.CASCADE)
    cantitate = models.IntegerField()


from phonenumber_field.modelfields import PhoneNumberField
from django.db import models

# Create your models here.


class Furnizor(models.Model):
    class Meta:
        verbose_name_plural = 'Furnizori'
    nume = models.CharField(max_length=50)
    adresa = models.CharField(max_length=255)
    categorie = models.CharField(max_length=255)
    companie = models.CharField(max_length=255)
    cui = models.CharField(max_length=9)  # mai pot lucra aici

    def __str__(self):
        return f'{self.nume}'


class Contact(models.Model):
    nume = models.CharField(max_length=50)
    nr_telefon = PhoneNumberField(null=True, default=None)
    email = models.EmailField()

    def __str__(self):
        return f'{self.nume}'


class ContactFurnizor(models.Model):
    furnizor = models.ForeignKey(Furnizor, on_delete=models.DO_NOTHING)
    persoana_de_contact = models.CharField(max_length=255)

    def __str__(self):
        return f'Firma: {self.furnizor}, contact: {self.persoana_de_contact}'


class FacturaAchizitie(models.Model):
    furnizor = models.ForeignKey(
        ContactFurnizor, on_delete=models.DO_NOTHING)
    nr_factura = models.BigIntegerField()  # trebuie sa fiu mai specific aici


class Produs(models.Model):
    nume_produs = models.CharField(max_length=55)
    ean = models.BigIntegerField()  # trebuie sa fiu mai specific aici
    serial_number = models.BigIntegerField()  # trebuie sa fiu mai specific aici
    producator = models.CharField(max_length=50)
    descriere = models.CharField(max_length=255)
    creat_la = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nume_produs}'


class ReceptieMarfa(models.Model):
    furnizor = models.ForeignKey(
        ContactFurnizor, on_delete=models.DO_NOTHING)
    data = models.DateTimeField(auto_now_add=True)
    receptionat_de = models.CharField(max_length=50)


class ProduseReceptionate(models.Model):
    receptie_marfa = models.CharField(max_length=2550)
    produs = models.ForeignKey(
        Produs, on_delete=models.DO_NOTHING)  # e bine aici?
    cantitate = models.IntegerField()

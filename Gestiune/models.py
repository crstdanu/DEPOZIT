
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Furnizor(models.Model):
    class Meta:
        verbose_name_plural = 'Furnizori'

    cui = models.CharField(max_length=9, unique=True)
    nume = models.CharField(max_length=100, default='')
    adresa = models.CharField(max_length=255, default='')
    numar_reg_com = models.CharField(max_length=15, default='')
    telefon = models.CharField(max_length=15, default='')

    # def populeaza_din_api(self):
    #     URL = f'https://api.openapi.ro/api/companies/{self.cui}'
    #     API_KEY = 'x9TYCaNAfuj-it3sami_hi82J8qEh3NyPVsqmLoE5pCBsaj3Mw'
    #     headers = {'x-api-key': API_KEY}
    #     try:
    #         response = requests.get(URL, headers=headers, timeout=10)
    #         data = response.json()
    #         self.nume = data.get('denumire')
    #         self.adresa = data.get('adresa')
    #         self.numar_reg_com = data.get('numar_reg_com')
    #         self.telefon = data.get('telefon')
    #         self.save()
    #     except Exception as e:
    #         print(f"S-a intamplat o eroare: {e}")

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     if not self.pk:
    #         self.populeaza_din_api()

    def __str__(self):
        return f'{self.nume}'


class Contact(models.Model):
    class Meta:
        verbose_name_plural = 'Contacte'

    nume = models.CharField(max_length=50)
    nr_telefon = models.CharField(max_length=13)
    email = models.EmailField()

    def __str__(self):
        return f'{self.nume}'


class ContactFurnizor(models.Model):
    class Meta:
        verbose_name_plural = 'Contact Furnizori'

    furnizor = models.ForeignKey(Furnizor, on_delete=models.CASCADE)
    persoana_de_contact = models.CharField(max_length=255)

    def __str__(self):
        return f'Firma: {self.furnizor}'


class FacturaAchizitie(models.Model):
    class Meta:
        verbose_name_plural = 'Facturi Achizitie'

    furnizor = models.ForeignKey(Furnizor, on_delete=models.CASCADE)
    nr_factura = models.BigIntegerField()
    valoare_factura = models.DecimalField(max_digits=10, decimal_places=2)
    data_factura = models.DateTimeField(auto_now_add=True)


class Produs(models.Model):
    class Meta:
        verbose_name_plural = 'Produse'

    nume_produs = models.CharField(max_length=55)

    ean = models.CharField(max_length=13)

    serial_number = models.CharField(max_length=15, default=None, null=True)
    producator = models.CharField(max_length=50)
    descriere = models.CharField(max_length=255)
    creat_la = models.DateTimeField(auto_now_add=True)
    cantitate_in_stoc = models.IntegerField(default=0)

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
    cantitate = models.PositiveIntegerField()


@receiver(post_save, sender=ProduseReceptionate)
def update_cantitate_in_stoc(sender, instance, created, **kwargs):
    if created:  # Check if a new instance of ProduseReceptionate is created
        produs = instance.produs  # Get the associated Produs instance
        # Update 'cantitate_in_stoc' by adding the value of 'cantitate' from ProduseReceptionate
        produs.cantitate_in_stoc += instance.cantitate
        produs.save()  # Save the Produs instance with the updated 'cantitate_in_stoc'

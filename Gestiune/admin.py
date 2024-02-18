from django.contrib import admin
from .models import *

# Register your models here.

admin.site.site_header = 'Sistem de management al inventarului'
admin.site.index_title = 'Panou de bord'


class FacturaAchizitieInLine(admin.StackedInline):
    model = FacturaAchizitie
    extra = 0


class FurnizorAdmin(admin.ModelAdmin):
    inlines = [FacturaAchizitieInLine]
    list_display = ['cui', 'nume', 'adresa', 'numar_reg_com', 'telefon']
    list_filter = ['nume']
    search_fields = ['nume', 'telefon', 'adresa',]


admin.site.register(Furnizor, FurnizorAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ['nume', 'nr_telefon', 'email']
    list_filter = ['email']
    search_fields = ['nume', 'nr_telefon', 'email']


admin.site.register(Contact, ContactAdmin)


class ContactFurnizorAdmin(admin.ModelAdmin):
    list_display = ['furnizor', 'persoana_de_contact']
    list_filter = ['furnizor', 'persoana_de_contact']
    search_fields = ['furnizor', 'persoana_de_contact']


admin.site.register(ContactFurnizor, ContactFurnizorAdmin)


class FacturaAchizitieAdmin(admin.ModelAdmin):
    list_display = ['furnizor', 'nr_factura',
                    'valoare_factura', 'data_factura']
    list_filter = ['valoare_factura', 'data_factura']
    date_hierarchy = 'data_factura'
    search_fields = ['furnizor', 'nr_factura',
                     'valoare_factura', 'data_factura']


admin.site.register(FacturaAchizitie, FacturaAchizitieAdmin)


class ProdusAdmin(admin.ModelAdmin):
    list_display = ['nume_produs', 'ean', 'producator',
                    'descriere', 'creat_la', 'cantitate_in_stoc']
    list_filter = ['nume_produs', 'producator',
                   'creat_la', 'cantitate_in_stoc']
    date_hierarchy = 'creat_la'
    search_fields = ['nume_produs', 'ean', 'producator',
                     'descriere', 'creat_la', 'cantitate_in_stoc']


admin.site.register(Produs, ProdusAdmin)


class ReceptieMarfaAdmin(admin.ModelAdmin):
    list_display = ['furnizor', 'data', 'receptionat_de']
    list_filter = ['furnizor', 'data', 'receptionat_de']
    date_hierarchy = 'data'
    search_fields = ['furnizor', 'data', 'receptionat_de']


admin.site.register(ReceptieMarfa, ReceptieMarfaAdmin)


class ProduseReceptionateAdmin(admin.ModelAdmin):
    fields = ('receptie_marfa', ('produs', 'cantitate'),)
    list_display = ['receptie_marfa', 'produs', 'cantitate']
    list_filter = ['produs', 'cantitate']
    search_fields = ['receptie_marfa', 'produs', 'cantitate']


admin.site.register(ProduseReceptionate, ProduseReceptionateAdmin)

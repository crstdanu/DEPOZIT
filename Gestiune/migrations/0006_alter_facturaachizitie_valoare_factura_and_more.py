# Generated by Django 5.0.1 on 2024-02-18 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gestiune', '0005_produs_cantitate_in_stoc_alter_furnizor_adresa_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facturaachizitie',
            name='valoare_factura',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='produsereceptionate',
            name='cantitate',
            field=models.PositiveIntegerField(),
        ),
    ]

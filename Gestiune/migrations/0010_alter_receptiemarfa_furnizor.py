# Generated by Django 5.0.1 on 2024-02-27 17:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gestiune', '0009_alter_receptiemarfa_furnizor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receptiemarfa',
            name='furnizor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestiune.furnizor'),
        ),
    ]

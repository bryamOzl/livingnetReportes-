# Generated by Django 4.1.2 on 2022-10-21 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("soportesLivingNet", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="problemaconfirmado",
            name="pcon_codigo",
            field=models.CharField(max_length=5, unique=True, verbose_name="Código"),
        ),
        migrations.AlterField(
            model_name="problemaconfirmado",
            name="pcon_problema",
            field=models.CharField(max_length=70, verbose_name="Tipo de problema"),
        ),
        migrations.AlterField(
            model_name="problemareportado",
            name="prep_codigo",
            field=models.CharField(max_length=5, unique=True, verbose_name="Código"),
        ),
        migrations.AlterField(
            model_name="problemareportado",
            name="prep_problema",
            field=models.CharField(max_length=70, verbose_name="Tipo de problema"),
        ),
    ]
# Generated by Django 4.1.2 on 2022-10-31 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("soportesLivingNet", "0002_alter_problemaconfirmado_pcon_codigo_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reporte",
            name="ProblemaConfirmado",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="pConfirmado",
                to="soportesLivingNet.problemaconfirmado",
                verbose_name="Problema Confirmado",
            ),
        ),
        migrations.AlterField(
            model_name="reporte",
            name="ProblemaReportado",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="pReportado",
                to="soportesLivingNet.problemareportado",
                verbose_name="Problema Reportado",
            ),
        ),
    ]
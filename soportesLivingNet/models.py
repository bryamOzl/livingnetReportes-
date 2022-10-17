from tabnanny import verbose
from django.db import models

# Create your models here.


class Contrato(models.Model):
    con_id_pk = models.AutoField(primary_key=True)
    con_sn = models.CharField(verbose_name='SN', max_length=70, blank=False)
    con_onu_type = models.CharField(
        verbose_name='ONU TYPE', max_length=100, blank=False)
    con_cod_contrato = models.CharField(
        verbose_name='Código de Contrato', max_length=100, blank=False, unique=True)
    con_nombre = models.CharField(
        verbose_name='Nombre del Cliente', max_length=100, blank=False)
    con_zona = models.CharField(
        verbose_name='Zona', max_length=100, blank=False)
    con_direccion = models.CharField(
        verbose_name='Dirección', max_length=100, blank=False)
    con_odb = models.CharField(verbose_name='ODB', max_length=100, blank=False)
    con_status = models.CharField(
        verbose_name='Estado', max_length=100, blank=False)

    class Meta:
        verbose_name = 'Contrato'
        verbose_name_plural = 'Contratos'

    def __str__(self):
        return self.con_cod_contrato + " " + self.con_nombre


class Reporte(models.Model):
    rep_id_pk = models.AutoField(primary_key=True)
    rep_pro_reportado = models.CharField(
        verbose_name='Problema Reportado', max_length=200, null=False, blank=False)
    rep_pro_tecnico = models.CharField(
        verbose_name='Problema Tècninico', max_length=200, null=False, blank=False)
    rep_estado = models.CharField(
        verbose_name='Estado', max_length=100, null=False, blank=False)
    rep_potencia = models.CharField(
        verbose_name='Potencia', max_length=70, null=False, blank=False)
    rep_ab_mikrotik = models.CharField(
        verbose_name='AB Mikrotik', max_length=70, null=False, blank=False)
    rep_observaciones = models.TextField(
        verbose_name='Observaciones', null=False, blank=False)
    Contrato_con_id = models.ForeignKey(Contrato, on_delete=models.CASCADE, verbose_name='Contrato',
                                        related_name='Contrato', null=False, blank=False)
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de creación")
    update = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Reporte"
        verbose_name_plural = "Reportes"

    def __str__(self):
        return self.Contrato_con_id.con_cod_contrato+ " " + self.Contrato_con_id.con_nombre

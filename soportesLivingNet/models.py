from email.policy import default
from random import choices
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


class Equipo(models.Model):
    equ_id_pk = models.AutoField(primary_key=True)
    equ_nombre = models.CharField(
        verbose_name='Equipo', max_length=30, blank=False, null=False)
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de creación")
    update = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'

    def __str__(self):
        return self.equ_nombre


class Casa(models.Model):
    cas_id_pk = models.AutoField(primary_key=True)
    cas_tipo = models.CharField(
        verbose_name='Tipo de casa', max_length=30, blank=False, null=False)
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de creación")
    update = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = 'Tipo de Casa'
        verbose_name_plural = 'Tipos de Casas'

    def __str__(self):
        return self.cas_tipo


class ProblemaReportado(models.Model):
    prep_id_pk = models.AutoField(primary_key=True)
    prep_codigo = models.CharField(
        unique=True, verbose_name='Código', max_length=5, blank=False, null=False)
    prep_problema = models.CharField(
        verbose_name='Tipo de problema', max_length=70, blank=False, null=False)
    create = models.DateTimeField(
        verbose_name='Fecha de creación', auto_now_add=True)
    update = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = 'Problema Reportado'
        verbose_name_plural = 'Problemas Reportados'

    def __str__(self):
        return self.prep_problema


class ProblemaConfirmado(models.Model):
    pcon_id_pk = models.AutoField(primary_key=True)
    pcon_codigo = models.CharField(
        unique=True, verbose_name='Código', max_length=5, blank=False, null=False)
    pcon_problema = models.CharField(
        verbose_name='Tipo de problema', max_length=70, blank=False, null=False)
    create = models.DateTimeField(
        verbose_name='Fecha de creación', auto_now_add=True)
    update = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = 'Problema Confirmado'
        verbose_name_plural = 'Problemas Confirmados'

    def __str__(self):
        return self.pcon_problema


class Reporte(models.Model):
    estado = [
        #('SELECCIONE', ''),
        ('SOLUCIONADO', 'SOLUCIONADO'),
        ('PENDIETE', 'PENDIETE'),
        ('OBSERVACIONES', 'OBSERVACIONES'),
    ]

    soporte = [
        ('TELEFONICO', 'TELEFONICO'),
        ('PRECENSIAL', 'PRECENSIAL'),
        ('NO CONTESTO', 'NO CONTESTO'),
    ]

    pon_range = range(1, 65, 1)
    pon = [('PON ' + str(i), 'PON ' + str(i)) for i in pon_range]

    rep_id_pk = models.AutoField(primary_key=True)
    """ rep_pro_reportado = models.CharField(
        verbose_name='Pro. Reportado', max_length=200, null=False, blank=False)
    rep_pro_tecnico = models.CharField(
        verbose_name='Pro. Tècninico', max_length=200, null=False, blank=False) """

    ProblemaReportado = models.ForeignKey(
        ProblemaReportado, on_delete=models.CASCADE, verbose_name='Problema Reportado', related_name='pReportado')
    ProblemaConfirmado = models.ForeignKey(
        ProblemaConfirmado, on_delete=models.CASCADE, verbose_name='Problema Confirmado', related_name='pConfirmado')

    rep_estado = models.CharField(choices=estado, default='PENDIETE',
                                  verbose_name='Estado', max_length=100, null=False, blank=False)

    #rep_nap = models.CharField(verbose_name='NAP', max_length=20, null=False, blank=False)
    rep_pon = models.CharField(
        max_length=20, choices=pon, verbose_name='PON', null=False, blank=False)
    rep_potencia_entrada = models.CharField(
        verbose_name='Pot Entrada', max_length=70, null=False, blank=False)
    rep_potencia_salida = models.CharField(
        verbose_name='Pot Salida', max_length=70, null=False, blank=False)
    Equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE,
                               verbose_name='Equipo', related_name='Equipo', null=False, blank=False)
    rep_ndispositivos = models.IntegerField(
        verbose_name='N° Dispositivos', blank=False, null=False)
    Casa = models.ForeignKey(
        Casa, on_delete=models.CASCADE, verbose_name='Tipo de Casa', related_name='Casa', null=False, blank=False)

    rep_ab_mikrotik = models.CharField(
        verbose_name='AB Mikrotik', max_length=70, null=False, blank=False)
    rep_tipo_soporte = models.CharField(
        choices=soporte, verbose_name='Tipo Soporte',  max_length=20, null=False, blank=False)
    rep_observaciones = models.TextField(
        verbose_name='Observaciones', null=False, blank=False)
    rep_imagen = models.FileField(
        upload_to='documentos/', verbose_name='Imagen', null=True, blank=True)
    Contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE, verbose_name='Contrato',
                                 related_name='Contrato', null=False, blank=False)
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de creación")
    update = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Reporte"
        verbose_name_plural = "Reportes"

    def __str__(self):
        return self.Contrato.con_cod_contrato + " " + self.Contrato.con_nombre

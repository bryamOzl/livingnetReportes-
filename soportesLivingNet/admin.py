from django.contrib import admin

from .models import Casa, Contrato, Equipo, ProblemaReportado, ProblemaConfirmado, Reporte

# Register your models here.

admin.site.site_header = 'LIVINGnet'
admin.site.index_title = 'LIVINGnet Soportes'
admin.site.site_title = 'Soportes'


class ContratoAdmin(admin.ModelAdmin):
    list_display = ('con_cod_contrato', 'con_nombre',
                    'con_zona', 'con_odb', 'con_status',)
    list_filter = ('con_zona', 'con_status')
    search_fields = ('con_cod_contrato', 'con_nombre',)
    ordering = ['con_id_pk']
    fields = [('con_cod_contrato', 'con_nombre'), 'con_sn', 'con_onu_type',
              'con_zona', 'con_direccion', 'con_odb', 'con_status']


class ReporteAdmin(admin.ModelAdmin):
    list_display = ['Contrato', 'zona', 'Equipo', 'rep_estado',
                    'pro_reportado', 'created']
    list_filter = ('rep_estado', 'ProblemaReportado')
    search_fields = ('Contrato__con_cod_contrato', 'created')
    autocomplete_fields = ['Contrato', 'Equipo', 'Casa',
                           'ProblemaReportado', 'ProblemaConfirmado']
    fields = [('ProblemaReportado', 'ProblemaConfirmado'),
              'rep_estado', 'rep_pon',
              ('rep_potencia_entrada', 'rep_potencia_salida'),
              ('rep_ndispositivos', 'rep_ab_mikrotik'),
              ('Equipo', 'Casa'),
              'rep_tipo_soporte', 'rep_observaciones', 'Contrato']

    def odb(self, obj):
        return obj.Contrato.con_odb

    def zona(self, obj):
        return obj.Contrato.con_zona

    def pro_reportado(self, obj):
        return obj.ProblemaReportado.prep_problema

    def pro_confirmado(self, obj):
        return obj.ProblemaConfirmado.pcon_problema


class EquipoAdmin(admin.ModelAdmin):
    list_display = ['equ_nombre', 'created', 'update']
    ordering = ['equ_nombre']
    search_fields = ('equ_nombre',)


class CasaAdmin(admin.ModelAdmin):
    list_display = ['cas_tipo', 'created', 'update']
    ordering = ['cas_tipo']
    search_fields = ('cas_tipo',)


class ProblemaReportadoAdmin(admin.ModelAdmin):
    list_display = ['prep_codigo', 'prep_problema', 'create', 'update']
    ordering = ['prep_problema']
    search_fields = ['prep_problema']


class ProblemaConfirmadoAdmin(admin.ModelAdmin):
    list_display = ['pcon_codigo', 'pcon_problema', 'create', 'update']
    ordering = ['pcon_problema']
    search_fields = ['pcon_problema']


admin.site.register(Contrato, ContratoAdmin)
admin.site.register(Reporte, ReporteAdmin)
admin.site.register(Equipo, EquipoAdmin)
admin.site.register(Casa, CasaAdmin)
admin.site.register(ProblemaReportado, ProblemaReportadoAdmin)
admin.site.register(ProblemaConfirmado, ProblemaConfirmadoAdmin)

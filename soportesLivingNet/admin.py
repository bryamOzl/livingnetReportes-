from django.contrib import admin

from .models import Casa, Contrato, Equipo, Reporte

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
    """ list_display = ['Contrato_con_id', 'rep_estado', 'rep_pro_reportado', 'rep_pro_tecnico',
                    'rep_pon', 'rep_potencia_entrada', 'rep_potencia_salida', 'Equipo_equ_id',
                    'rep_ndispositivos', 'rep_ab_mikrotik', 'Casa_cas_id', 'update'] """
    list_display = ['Contrato_con_id', 'odb', 'rep_estado', 'rep_pro_reportado',
                    'rep_pro_tecnico', 'update']
    #ordering = ('-publication_date',)
    list_filter = ('rep_estado',)
    search_fields = ('Contrato_con_id__con_cod_contrato',)
    autocomplete_fields = ['Contrato_con_id', 'Equipo_equ_id', 'Casa_cas_id']
    fields = ['rep_pro_reportado', 'rep_pro_tecnico', 'rep_estado', 'rep_pon',
              ('rep_potencia_entrada', 'rep_potencia_salida'),
              ('rep_ndispositivos', 'rep_ab_mikrotik'),
              ('Equipo_equ_id', 'Casa_cas_id'),
              'rep_observaciones', 'Contrato_con_id']
    
    def odb(self, obj):
        return obj.Contrato_con_id.con_odb


class EquipoAdmin(admin.ModelAdmin):
    list_display = ['equ_nombre', 'created', 'update']
    ordering = ['equ_nombre']
    search_fields = ('equ_nombre',)


class CasaAdmin(admin.ModelAdmin):
    list_display = ['cas_tipo', 'created', 'update']
    ordering = ['cas_tipo']
    search_fields = ('cas_tipo',)


admin.site.register(Contrato, ContratoAdmin)
admin.site.register(Reporte, ReporteAdmin)
admin.site.register(Equipo, EquipoAdmin)
admin.site.register(Casa, CasaAdmin)

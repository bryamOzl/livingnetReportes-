from django.contrib import admin

from .models import Contrato, Reporte

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
    list_display = ['Contrato_con_id', 'rep_estado', 'rep_pro_reportado', 'rep_potencia',
                    'rep_ab_mikrotik', 'created', 'update']
    #ordering = ('-publication_date',)
    list_filter = ('rep_estado',)
    search_fields = ('Contrato_con_id__con_cod_contrato',)
    autocomplete_fields = ["Contrato_con_id"]
    fields = ['rep_pro_reportado', 'rep_pro_tecnico', 'rep_estado',
              ('rep_potencia', 'rep_ab_mikrotik'), 'rep_observaciones', 'Contrato_con_id']


admin.site.register(Contrato, ContratoAdmin)
admin.site.register(Reporte, ReporteAdmin)

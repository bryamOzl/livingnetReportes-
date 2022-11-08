from django.contrib.admin.views.decorators import staff_member_required
from django.db.models.functions import ExtractYear, ExtractMonth
from django.http import JsonResponse

from django.shortcuts import render
import re

from soportesLivingNet.models import Reporte
from utils.charts import months, generate_color_palette

# Create your views here.


def clean(text):
    cadena = str(text)
    cadena_clean = re.sub(r"[^a-zA-Z0-9]", " ", cadena)
    cadena_new = cadena_clean.strip()
    return cadena_new


""" Sacar en grupo los anios de los contratos """


@staff_member_required
def get_filter_year(request):
    grupo_contratos = Reporte.objects.annotate(
        year=ExtractYear('created')).values('year').order_by('-year').distinct()
    options = [contratos['year'] for contratos in grupo_contratos]

    return JsonResponse({
        'options': options,
    })


""" Sacar en grupo los meses de los contratos """
@staff_member_required
def get_filter_month(request):
    mesesList = []
    grupo_contratos = Reporte.objects.annotate(
        month=ExtractMonth('created')).values('month').order_by('month').distinct()
    options = [contratos['month'] for contratos in grupo_contratos]
    for j in options:
        mesesList.append(months[j-1])
    return JsonResponse({
        'options': mesesList,
    })


@staff_member_required
def graph_reports_zones(request, year, month):
    reportes = Reporte.objects.filter(created__year=year, created__month=month)
    zonaList = []
    zonaNumero = []
    nreportes = 0
    zonas = reportes.values_list('Contrato__con_zona').distinct()
    for z in zonas:
        zonaList.append(clean(z))

    for n in zonaList:
        numero = reportes.filter(Contrato__con_zona=n).count(),
        zonaNumero.append(int(clean(numero)))
        nreportes = nreportes + int(clean(numero))

    # print(month)
    palette = generate_color_palette(len(zonaNumero))

    return JsonResponse({
        'data': {
            #'title': f'GRAFICA DE REPORTES POR ZONA EN EL MES DE {months[month-1]} DEL {year} TOTAL DE REPORTES : {str(nreportes)}',
            'title': f'TOTAL DE REPORTES {str(nreportes)} EN EL MES DE {months[month-1]} DEL {year}',
            'text' : 'aqui va texto',
            'labels': zonaList,
            'datasets': [{
                'label': 'NUMERO DE REPORTES POR ZONA',
                'backgroundColor': palette,
                'borderColor': palette,
                'data': zonaNumero,
            }]
        },
    })


@staff_member_required
def graph_reports_equipos(request, year, month):
    reportes = Reporte.objects.filter(created__year=year, created__month=month)
    equipoList = []
    equipoNumero = []
    nreportes = 0
    equipos = reportes.values_list('Equipo__equ_nombre').distinct()
    for e in equipos:
        objetoEquipo = str(e)
        stringEquipo = objetoEquipo.replace(
            "(", "").replace(")", "").replace(",", "").replace("'", "")
        equipoList.append(stringEquipo)

    for n in equipoList:
        numero = reportes.filter(Equipo__equ_nombre=n).count(),
        equipoNumero.append(int(clean(numero)))
        nreportes = nreportes + int(clean(numero))
    # print(month)
    palette = generate_color_palette(len(equipoNumero))

    return JsonResponse({
        'data': {
            #'title': f'GRAFICA DE REPORTES POR EQUIPO EN EL MES DE {months[month-1]} DEL {year}',
            'title': f'EL TOTAL DE REPORTES ES DE {str(nreportes)} EN EL MES DE {months[month-1]} DEL {year}',
            'labels': equipoList,
            'datasets': [{
                'label': 'NUMERO DE REPORTES POR EQUIPO',
                'backgroundColor': palette,
                'borderColor': palette,
                'data': equipoNumero,
            }]
        },
    })


@staff_member_required
def graph_reports_problema(request, year, month):
    reportes = Reporte.objects.filter(created__year=year, created__month=month)
    problemaList = []
    problemaNumero = []
    nreportes = 0
    problemas = reportes.values_list(
        'ProblemaReportado__prep_problema').distinct()
    for p in problemas:
        objetoEquipo = str(p)
        stringEquipo = objetoEquipo.replace(
            "(", "").replace(")", "").replace(",", "").replace("'", "")
        problemaList.append(stringEquipo)

    for n in problemaList:
        numero = reportes.filter(ProblemaReportado__prep_problema=n).count(),
        problemaNumero.append(int(clean(numero)))
        nreportes = nreportes + int(clean(numero))

    # print(month)
    palette = generate_color_palette(len(problemaNumero))

    return JsonResponse({
        'data': {
            #'title': f'GRAFICA DE REPORTES POR PROBLEMA REPORTADO EN EL MES DE {months[month-1]} DEL {year}',
            'title': f'EL TOTAL DE REPORTES ES DE {str(nreportes)} EN EL MES DE {months[month-1]} DEL {year}',
            'labels': problemaList,
            'datasets': [{
                'label': 'NUMERO DE REPORTES POR EQUIPO',
                'backgroundColor': palette,
                'borderColor': palette,
                'data': problemaNumero,
            }]
        },
    })


@staff_member_required
def statistics_view(request):
    return render(request, 'estadisticas.html', {})


@staff_member_required
def home_view(request):
    return render(request, 'home.html', {})

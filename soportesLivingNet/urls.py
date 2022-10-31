from django.urls import path


from . import views

urlpatterns = [
    path('estadisticas/', views.statistics_view, name='estadisticas'),  # new
    path('anio/', views.get_filter_year, name='anio'),
    path('month/', views.get_filter_month, name='month'),
    path('graficasZona/<int:year>/<int:month>/',
         views.graph_reports_zones, name='graficasZona'),
    path('graficasEquipos/<int:year>/<int:month>/',
         views.graph_reports_equipos, name='graficasEquipos'),
    path('graficasProblemas/<int:year>/<int:month>/',
         views.graph_reports_problema, name='graficasProblemas'),
]

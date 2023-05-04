from django.urls import path
from historia_clinica.views import HistoriaClinicaCreateView, HistoriaClinicaListView
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HistoriaClinicaCreateView.as_view(), name='crear_historia_clinica'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('crear_historia_clinica/', HistoriaClinicaCreateView.as_view(), name='crear_historia_clinica'),
    path('lista_historias_clinicas/', HistoriaClinicaListView.as_view(), name='lista_historias_clinicas'),
]

from django.contrib.auth.views import LogoutView
from django.urls import path, include
from django.contrib import admin
from historia_clinica.views import CustomLoginView, CustomUserCreationView, HistoriaClinicaCreateView, HistoriaClinicaListView,profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CustomLoginView.as_view(), name='login'), 
    path('register/', CustomUserCreationView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('crear_historia_clinica/', HistoriaClinicaCreateView.as_view(), name='crear_historia_clinica'),
    path('lista_historias_clinicas/', HistoriaClinicaListView.as_view(), name='lista_historias_clinicas'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', profile, name='profile'),
]
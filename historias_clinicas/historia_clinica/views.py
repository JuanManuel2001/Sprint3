# views.py

from django.shortcuts import redirect, render
from django.views import View
from .models import HistoriaClinica, Paciente, Medico
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    return render(request, 'registration/profile.html')


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('crear_historia_clinica')

class CustomUserCreationView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'





class HistoriaClinicaCreateView(View):
    def get(self, request):
        return render(request, 'crear_historia_clinica.html')

    def post(self, request):
        # Obtener los datos del formulario
        paciente_nombre = request.POST.get('paciente_nombre')
        paciente_apellido = request.POST.get('paciente_apellido')
        paciente_fecha_nacimiento = request.POST.get('paciente_fecha_nacimiento')
        paciente_dni = request.POST.get('paciente_dni')
        paciente_obra_social = request.POST.get('paciente_obra_social')

        medico_nombre = request.POST.get('medico_nombre')
        medico_apellido = request.POST.get('medico_apellido')
        medico_especialidad = request.POST.get('medico_especialidad')
        medico_matricula = request.POST.get('medico_matricula')

        fecha = request.POST.get('fecha')
        descripcion = request.POST.get('descripcion')

        # Verificar que se proporcionaron valores para el nombre y el apellido del paciente
        if not paciente_nombre or not paciente_apellido:
            # Si no se proporcionaron ambos valores, redirigir al usuario de vuelta al formulario
            return render(request, 'crear_historia_clinica.html', {'error': 'Debe ingresar el nombre y el apellido del paciente'})

        # Crear los objetos de Paciente, Medico y HistoriaClinicaAuditada
        paciente = Paciente(
            nombre=paciente_nombre,
            apellido=paciente_apellido,
            fecha_nacimiento=paciente_fecha_nacimiento,
            dni=paciente_dni,
            obra_social=paciente_obra_social,
        )
        paciente.save()

        medico = Medico(
            nombre=medico_nombre,
            apellido=medico_apellido,
            especialidad=medico_especialidad,
            matricula=medico_matricula,
        )

        historia_clinica = HistoriaClinica(
            paciente=paciente,
            medico=medico,
            fecha=fecha,
            descripcion=descripcion,
        )

        # Guardar los objetos en la base de datos
        medico.save()
        historia_clinica.save()

        # Redirigir al usuario a la página de lista de historias clínicas
        return redirect('lista_historias_clinicas')



class HistoriaClinicaListView(View):
    def get(self, request):
        historias_clinicas = HistoriaClinica.objects.all()
        return render(request, 'lista_historias_clinicas.html', {'historias_clinicas': historias_clinicas})

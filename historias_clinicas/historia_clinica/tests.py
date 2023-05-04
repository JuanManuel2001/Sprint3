from django.test import TestCase
from historia_clinica.models import Paciente, Medico, HistoriaClinica
from datetime import date, timedelta
from django.core.exceptions import ValidationError


class PacienteModelTest(TestCase):
    def test_fecha_nacimiento_no_futura(self):
        fecha_futura = date.today() + timedelta(days=1)
        paciente = Paciente(nombre='Nombre', apellido='Apellido', fecha_nacimiento=fecha_futura, dni='12345678', obra_social='obra social')
        with self.assertRaises(ValidationError):
            paciente.full_clean()



class MedicoModelTest(TestCase):
    def test_nombre_completo(self):
        medico = Medico.objects.create(
            nombre='nombre',
            apellido='apellido',
            especialidad='especialidad',
            matricula='matricula'
        )
        self.assertEqual(medico.nombre, 'nombre')


class HistoriaClinicaModelTest(TestCase):
    def test_str(self):
        paciente = Paciente.objects.create(
            nombre='nombre',
            apellido='apellido',
            fecha_nacimiento='1990-01-01',
            dni='12345678',
            obra_social='obra social'
        )
        medico = Medico.objects.create(
            nombre='nombre',
            apellido='apellido',
            especialidad='especialidad',
            matricula='matricula'
        )
        historia_clinica = HistoriaClinica.objects.create(
            paciente=paciente,
            medico=medico,
            fecha='2022-05-04',
            descripcion='descripción de la historia clínica'
        )
        self.assertEqual(str(historia_clinica), f'{paciente} - {medico} - 2022-05-04')
from django.test import TestCase
from django.urls import reverse
from django.test.utils import override_settings

class SecurityTest(TestCase):

    def test_csrf(self):
        response = self.client.get(reverse('crear_historia_clinica'))
        csrf_token = response.cookies['csrftoken'].value
        response = self.client.post(reverse('crear_historia_clinica'), {'csrfmiddlewaretoken': csrf_token})
        self.assertEqual(response.status_code, 200)

    @override_settings(DEBUG=False)
    def test_debug(self):
        response = self.client.get(reverse('crear_historia_clinica'))
        self.assertEqual(response.status_code, 200)


    def test_xss(self):
        payload = '<script>alert("XSS")</script>'
        response = self.client.post(reverse('crear_historia_clinica'), {'descripcion': payload})
        self.assertNotContains(response, payload)

    def test_sql_injection(self):
        payload = "'; DROP TABLE historias_clinicas_paciente;--"
        response = self.client.post(reverse('crear_historia_clinica'), {'descripcion': payload})
        self.assertNotContains(response, payload)

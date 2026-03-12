from django.test import TestCase
from django.urls import reverse

from .forms import CamaraForm
from .models import Camara

# ---------------------------------------------------------------------------
# Datos de prueba reutilizables
# ---------------------------------------------------------------------------

CAMARA_VALIDA = {
    'empresa': 'TestEmpresa',
    'nombre': 'Cam-01',
    'modelo': 'DS-2CD2143G2-I',
    'serie': 'ABC123',
    'ip': '192.168.1.100',
    'mac': 'AA:BB:CC:DD:EE:FF',
}


def crear_camara(**kwargs) -> Camara:
    """Crea y retorna una instancia Camara usando los datos base CAMARA_VALIDA."""
    datos = {**CAMARA_VALIDA, **kwargs}
    return Camara.objects.create(**datos)


# ---------------------------------------------------------------------------
# Tests de Modelo
# ---------------------------------------------------------------------------

class CamaraModelTest(TestCase):

    def test_str_returns_nombre(self):
        camara = crear_camara()
        self.assertEqual(str(camara), 'Cam-01')

    def test_ordering_desc_created_at(self):
        """El ordering del Meta es -created_at; la camara mas reciente va primero."""
        primera = crear_camara(nombre='Cam-Antigua', serie='S001', ip='192.168.1.1')
        segunda = crear_camara(nombre='Cam-Nueva', serie='S002', ip='192.168.1.2')

        qs = list(Camara.objects.all())

        self.assertEqual(qs[0].pk, segunda.pk)
        self.assertEqual(qs[1].pk, primera.pk)


# ---------------------------------------------------------------------------
# Tests de Formulario
# ---------------------------------------------------------------------------

class CamaraFormTest(TestCase):

    def test_form_valid_with_correct_mac(self):
        form = CamaraForm(data=CAMARA_VALIDA)
        self.assertTrue(form.is_valid(), msg=form.errors)

    def test_form_invalid_with_bad_mac(self):
        datos = {**CAMARA_VALIDA, 'mac': 'AABBCCDDEEFF'}
        form = CamaraForm(data=datos)
        self.assertFalse(form.is_valid())
        self.assertIn('mac', form.errors)

    def test_form_invalid_with_empty_fields(self):
        form = CamaraForm(data={})
        self.assertFalse(form.is_valid())
        for field in ['empresa', 'nombre', 'modelo', 'serie', 'ip', 'mac']:
            self.assertIn(field, form.errors, msg=f'Se esperaba error en campo: {field}')

    def test_mac_normalized_to_uppercase(self):
        datos = {**CAMARA_VALIDA, 'mac': 'aa:bb:cc:dd:ee:ff'}
        form = CamaraForm(data=datos)
        self.assertTrue(form.is_valid(), msg=form.errors)
        self.assertEqual(form.cleaned_data['mac'], 'AA:BB:CC:DD:EE:FF')


# ---------------------------------------------------------------------------
# Tests de Vistas
# ---------------------------------------------------------------------------

class CamaraViewTest(TestCase):

    def setUp(self):
        self.camara = crear_camara()

    # --- lista_camaras ---

    def test_lista_camaras_status_200(self):
        response = self.client.get(reverse('lista_camaras'))
        self.assertEqual(response.status_code, 200)

    # --- registrar_camara ---

    def test_registrar_camara_get_status_200(self):
        response = self.client.get(reverse('registrar_camara'))
        self.assertEqual(response.status_code, 200)

    def test_registrar_camara_post_valid(self):
        datos = {
            **CAMARA_VALIDA,
            'nombre': 'Cam-02',
            'serie': 'XYZ789',
            'ip': '10.0.0.1',
        }
        response = self.client.post(reverse('registrar_camara'), data=datos)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('lista_camaras'))
        self.assertEqual(Camara.objects.count(), 2)

    def test_registrar_camara_post_invalid_mac(self):
        datos = {**CAMARA_VALIDA, 'mac': 'INVALIDA', 'serie': 'NEW001', 'ip': '10.0.0.2'}
        response = self.client.post(reverse('registrar_camara'), data=datos)

        self.assertEqual(response.status_code, 200)
        self.assertIn('form', response.context)
        self.assertTrue(response.context['form'].errors)
        self.assertIn('mac', response.context['form'].errors)

    # --- editar_camara ---

    def test_editar_camara_get_status_200(self):
        url = reverse('editar_camara', kwargs={'pk': self.camara.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_editar_camara_post_valid(self):
        url = reverse('editar_camara', kwargs={'pk': self.camara.pk})
        datos = {**CAMARA_VALIDA, 'nombre': 'Cam-Editada'}
        response = self.client.post(url, data=datos)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('lista_camaras'))
        self.camara.refresh_from_db()
        self.assertEqual(self.camara.nombre, 'Cam-Editada')

    # --- eliminar_camara ---

    def test_eliminar_camara_get_status_200(self):
        url = reverse('eliminar_camara', kwargs={'pk': self.camara.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_eliminar_camara_post_elimina(self):
        url = reverse('eliminar_camara', kwargs={'pk': self.camara.pk})
        response = self.client.post(url)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('lista_camaras'))
        self.assertFalse(Camara.objects.filter(pk=self.camara.pk).exists())

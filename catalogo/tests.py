from django.test import TestCase

from .models import Catalogo, Categoria


class InicioViewTests(TestCase):
    def test_muestra_mensaje_si_no_hay_productos(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Aún no hay productos")

    def test_muestra_productos_y_sus_categorias(self):
        producto = Catalogo.objects.create(
            nombre="Notebook",
            descripcion="Equipo para trabajo y estudio",
            precio="599990.00",
        )
        Categoria.objects.create(
            nombre="Computación",
            descripcion="Notebooks y accesorios",
            foreign_key=producto,
        )

        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Notebook")
        self.assertContains(response, "Computación")
        self.assertContains(response, "Equipo para trabajo y estudio")


class DetalleProductoViewTests(TestCase):
    def setUp(self):
        self.producto = Catalogo.objects.create(
            nombre="Notebook",
            descripcion="Equipo para trabajo y estudio",
            precio="599990.00",
        )
        Categoria.objects.create(
            nombre="Computación",
            descripcion="Notebooks y accesorios",
            foreign_key=self.producto,
        )

    def test_muestra_producto_por_nombre(self):
        response = self.client.get(f"/producto/{self.producto.nombre}/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Notebook")
        self.assertContains(response, "Computación")
        self.assertContains(response, "599990")

    def test_id_inexistente_devuelve_404(self):
        response = self.client.get("/producto/Producto-inexistente/")

        self.assertEqual(response.status_code, 404)
        self.assertContains(response, "¡Ups! Nos perdimos entre tantos gatos.", status_code=404)

import pytest
from src.models.concretos.silla import Silla


class TestSilla:
    @pytest.fixture
    def silla_basica(self):
        """Fixture para crear una silla básica de prueba"""
        return Silla("Silla Básica", "Madera", 50.0, 4, "Madera")

    def test_instanciacion_correcta(self, silla_basica):
        """Verificar que la silla se instancia correctamente con todos sus atributos"""
        # Verificar herencia de atributos de Mueble
        assert silla_basica.nombre == "Silla Básica"
        assert silla_basica.material == "Madera"
        assert silla_basica.precio_base == 50.0

        # Verificar atributos específicos de Asientos
        assert silla_basica.numero_patas == 4

        # Verificar atributos específicos de Silla
        assert silla_basica.tipo_madera == "Madera"

    def test_calcular_precio(self, silla_basica):
        """Probar el cálculo del precio de la silla (polimorfismo)"""
        precio = silla_basica.calcular_precio()
        assert precio == 50.0  # Precio base sin modificaciones
        assert isinstance(precio, float)

    def test_obtener_descripcion(self, silla_basica):
        """Verificar que la descripción contiene la información correcta"""
        descripcion = silla_basica.obtener_descripcion()
        assert "Silla Básica" in descripcion
        assert "Madera" in descripcion
        assert isinstance(descripcion, str)

    @pytest.mark.parametrize(
        "material,tipo_madera,precio",
        [
            ("Pino", "Pino", 40.0),
            ("Roble", "Roble", 80.0),
            ("Caoba", "Caoba", 120.0),
            ("Cerezo", "Cerezo", 100.0),
        ],
    )
    def test_diferentes_tipos_madera(self, material, tipo_madera, precio):
        """Probar sillas con diferentes tipos de madera"""
        silla = Silla(f"Silla {tipo_madera}", material, precio, 4, tipo_madera)
        assert silla.material == material
        assert silla.tipo_madera == tipo_madera
        assert silla.calcular_precio() == precio

    def test_silla_tres_patas(self):
        """Probar silla con tres patas"""
        silla = Silla("Silla Moderna", "Metal", 60.0, 3, "N/A")
        assert silla.numero_patas == 3

    def test_silla_metal(self):
        """Probar silla de metal"""
        silla = Silla("Silla Metal", "Metal", 70.0, 4, "N/A")
        assert silla.material == "Metal"
        assert silla.tipo_madera == "N/A"

    def test_silla_precio_bajo(self):
        """Probar silla con precio bajo"""
        silla = Silla("Silla Económica", "Plástico", 20.0, 4, "N/A")
        assert silla.calcular_precio() == 20.0

    def test_silla_precio_alto(self):
        """Probar silla con precio alto"""
        silla = Silla("Silla Premium", "Caoba", 200.0, 4, "Caoba")
        assert silla.calcular_precio() == 200.0

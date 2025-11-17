import pytest
from src.models.concretos.silla import Silla


class TestSilla:
    @pytest.fixture
    def silla_basica(self):
        """Fixture para crear una silla básica de prueba"""
        return Silla("Silla Básica", "Madera", "Café", 50.0, True, "Tela", False, False)

    def test_instanciacion_correcta(self, silla_basica):
        """Verificar que la silla se instancia correctamente con todos sus atributos"""
        # Verificar herencia de atributos de Mueble
        assert silla_basica.nombre == "Silla Básica"
        assert silla_basica.material == "Madera"
        assert silla_basica.color == "Café"
        assert silla_basica.precio_base == 50.0

        # Verificar atributos específicos de Asiento
        assert silla_basica.capacidad_personas == 1
        assert silla_basica.tiene_respaldo == True

    def test_calcular_precio(self, silla_basica):
        """Probar el cálculo del precio de la silla (polimorfismo)"""
        precio = silla_basica.calcular_precio()
        assert precio > 0  # Precio debe ser positivo
        assert isinstance(precio, float)

    def test_obtener_descripcion(self, silla_basica):
        """Verificar que la descripción contiene la información correcta"""
        descripcion = silla_basica.obtener_descripcion()
        assert "Silla Básica" in descripcion
        assert "Madera" in descripcion
        assert isinstance(descripcion, str)

    @pytest.mark.parametrize(
        "material,precio",
        [
            ("Pino", 40.0),
            ("Roble", 80.0),
            ("Caoba", 120.0),
            ("Cerezo", 100.0),
        ],
    )
    def test_diferentes_materiales(self, material, precio):
        """Probar sillas con diferentes materiales"""
        silla = Silla(f"Silla {material}", material, "Natural", precio, True, "Tela")
        assert silla.material == material
        assert silla.calcular_precio() > 0

    def test_silla_con_ruedas(self):
        """Probar silla con ruedas"""
        silla = Silla(
            "Silla Oficina", "Metal", "Negro", 90.0, True, "Cuero", True, True
        )
        assert silla.altura_regulable == True
        assert silla.tiene_ruedas == True

    def test_silla_metal(self):
        """Probar silla de metal"""
        silla = Silla("Silla Metal", "Metal", "Gris", 70.0, True, "Tela")
        assert silla.material == "Metal"

    def test_silla_precio_bajo(self):
        """Probar silla con precio bajo"""
        silla = Silla("Silla Económica", "Plástico", "Blanco", 20.0, True, "Tela")
        assert silla.calcular_precio() > 0

    def test_silla_precio_alto(self):
        """Probar silla con precio alto"""
        silla = Silla(
            "Silla Premium", "Caoba", "Café Oscuro", 200.0, True, "Cuero", True, False
        )
        assert silla.calcular_precio() > 0

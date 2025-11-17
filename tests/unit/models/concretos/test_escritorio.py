import pytest
from src.models.concretos.escritorio import Escritorio


class TestEscritorio:
    @pytest.fixture
    def escritorio_basico(self):
        """Fixture para crear un escritorio básico de prueba"""
        return Escritorio(
            "Escritorio Oficina",
            "Madera",
            "Café",
            250,
            "rectangular",
            True,
            2,
            1.2,
            False,
        )

    def test_instanciacion_correcta(self, escritorio_basico):
        """Verificar que el escritorio se instancia correctamente con todos sus atributos"""
        assert escritorio_basico.nombre == "Escritorio Oficina"
        assert escritorio_basico.material == "Madera"
        assert escritorio_basico.color == "Café"
        assert escritorio_basico.precio_base == 250
        assert escritorio_basico.forma == "rectangular"
        assert escritorio_basico.tiene_cajones == True
        assert escritorio_basico.num_cajones == 2

    def test_calcular_precio(self, escritorio_basico):
        """Probar el cálculo del precio del escritorio"""
        precio = escritorio_basico.calcular_precio()
        # Precio: 250 + (2 cajones * 25) = 300
        assert precio == 300
        assert isinstance(precio, int)

    def test_obtener_descripcion(self, escritorio_basico):
        """Verificar que la descripción contiene la información correcta"""
        descripcion = escritorio_basico.obtener_descripcion()
        assert "Escritorio Oficina" in descripcion
        assert "Madera" in descripcion
        assert isinstance(descripcion, str)

    def test_escritorio_sin_cajones(self):
        """Probar escritorio sin cajones"""
        escritorio = Escritorio(
            "Escritorio Simple", "Metal", "Gris", 150, "rectangular", False, 0
        )
        assert escritorio.tiene_cajones == False
        assert escritorio.num_cajones == 0

    def test_escritorio_con_iluminacion(self):
        """Probar escritorio con iluminación"""
        escritorio = Escritorio(
            "Escritorio LED",
            "Madera",
            "Blanco",
            300,
            "rectangular",
            False,
            0,
            1.2,
            True,
        )
        # Precio: 300 + 40 (iluminación) = 340
        assert escritorio.calcular_precio() == 340

    def test_escritorio_grande(self):
        """Probar escritorio grande"""
        escritorio = Escritorio(
            "Escritorio Ejecutivo", "Roble", "Negro", 400, "L", True, 4, 1.8, True
        )
        # Precio: 400 + (4*25) + 50 (largo>1.5) + 40 (ilum) + 30 (forma) = 620
        assert escritorio.calcular_precio() == 620

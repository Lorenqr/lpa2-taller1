import pytest
from src.models.concretos.cajonera import Cajonera


class TestCajonera:
    @pytest.fixture
    def cajonera_basica(self):
        """Fixture para crear una cajonera básica de prueba"""
        return Cajonera("Cajonera Estándar", "Madera", "Blanco", 150, 5)
    
    def test_instanciacion_correcta(self, cajonera_basica):
        """Verificar que la cajonera se instancia correctamente con todos sus atributos"""
        assert cajonera_basica.nombre == "Cajonera Estándar"
        assert cajonera_basica.material == "Madera"
        assert cajonera_basica.color == "Blanco"
        assert cajonera_basica.precio_base == 150
        assert cajonera_basica.num_cajones == 5
    
    def test_calcular_precio(self, cajonera_basica):
        """Probar el cálculo del precio de la cajonera"""
        precio = cajonera_basica.calcular_precio()
        # Precio: 150 + (5 cajones * 30) = 300
        assert precio == 300
        assert isinstance(precio, int)
    
    def test_obtener_descripcion(self, cajonera_basica):
        """Verificar que la descripción contiene la información correcta"""
        descripcion = cajonera_basica.obtener_descripcion()
        assert "Cajonera Estándar" in descripcion
        assert "Madera" in descripcion
        assert isinstance(descripcion, str)
    
    def test_cajonera_muchos_cajones(self):
        """Probar cajonera con muchos cajones"""
        cajonera = Cajonera("Cajonera Grande", "Roble", "Natural", 250, 10)
        assert cajonera.num_cajones == 10
        # Precio: 250 + (10 * 30) = 550
        assert cajonera.calcular_precio() == 550

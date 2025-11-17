import pytest
from src.models.concretos.mesa import Mesa


class TestMesa:
    @pytest.fixture
    def mesa_basica(self):
        """Fixture para crear una mesa básica de prueba"""
        return Mesa("Mesa Comedor", "Madera", "Café", 200.0, "rectangular", 120.0, 80.0, 75.0, 6)
    
    def test_instanciacion_correcta(self, mesa_basica):
        """Verificar que la mesa se instancia correctamente con todos sus atributos"""
        assert mesa_basica.nombre == "Mesa Comedor"
        assert mesa_basica.material == "Madera"
        assert mesa_basica.color == "Café"
        assert mesa_basica.precio_base == 200.0
        assert mesa_basica.forma == "rectangular"
        assert mesa_basica.capacidad_personas == 6
    
    def test_calcular_precio(self, mesa_basica):
        """Probar el cálculo del precio de la mesa"""
        precio = mesa_basica.calcular_precio()
        assert precio > 0
        assert isinstance(precio, float)
    
    def test_obtener_descripcion(self, mesa_basica):
        """Verificar que la descripción contiene la información correcta"""
        descripcion = mesa_basica.obtener_descripcion()
        assert "Mesa Comedor" in descripcion
        assert "Madera" in descripcion
        assert isinstance(descripcion, str)
    
    def test_mesa_pequeña(self):
        """Probar mesa con capacidad pequeña"""
        mesa = Mesa("Mesa Pequeña", "Metal", "Gris", 100.0, "redonda", 90.0, 90.0, 75.0, 2)
        assert mesa.capacidad_personas == 2
    
    def test_mesa_grande(self):
        """Probar mesa con capacidad grande"""
        mesa = Mesa("Mesa Grande", "Roble", "Natural", 500.0, "rectangular", 200.0, 100.0, 75.0, 12)
        assert mesa.capacidad_personas == 12

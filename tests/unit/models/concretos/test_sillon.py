import pytest
from src.models.concretos.sillon import Sillon


class TestSillon:
    @pytest.fixture
    def sillon_basico(self):
        """Fixture para crear un sillón básico de prueba"""
        return Sillon("Sillón Reclinable", "Cuero", "Café", 350, 2, True, "Cuero", True, True, False)
    
    def test_instanciacion_correcta(self, sillon_basico):
        """Verificar que el sillón se instancia correctamente con todos sus atributos"""
        assert sillon_basico.nombre == "Sillón Reclinable"
        assert sillon_basico.material == "Cuero"
        assert sillon_basico.color == "Café"
        assert sillon_basico.precio_base == 350
        assert sillon_basico.capacidad_personas == 2
        assert sillon_basico.es_reclinable == True
    
    def test_calcular_precio(self, sillon_basico):
        """Probar el cálculo del precio del sillón"""
        precio = sillon_basico.calcular_precio()
        # Precio: 350 + 200 (tapizado) + 100 (brazos) + 250 (reclinable) = 900
        assert precio == 900
        assert isinstance(precio, int)
    
    def test_obtener_descripcion(self, sillon_basico):
        """Verificar que la descripción contiene la información correcta"""
        descripcion = sillon_basico.obtener_descripcion()
        assert "Sillón Reclinable" in descripcion
        assert "Cuero" in descripcion
        assert isinstance(descripcion, str)
    
    def test_sillon_reclinable(self):
        """Probar sillón con función reclinable"""
        sillon = Sillon("Sillón Comfort", "Tela", "Gris", 300, 2, True, "Tela", True, True, False)
        assert sillon.es_reclinable == True
    
    def test_sillon_no_reclinable(self):
        """Probar sillón sin función reclinable"""
        sillon = Sillon("Sillón Básico", "Tela", "Azul", 250, 2, True, "Tela", True, False, False)
        assert sillon.es_reclinable == False
    
    def test_sillon_con_reposapiés(self):
        """Probar sillón con reposapiés"""
        sillon = Sillon("Sillón Relax", "Cuero", "Negro", 400, 1, True, "Cuero", True, True, True)
        assert sillon.tiene_reposapiés == True

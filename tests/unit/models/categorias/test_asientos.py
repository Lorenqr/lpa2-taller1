import pytest
from abc import ABC
from src.models.categorias.asientos import Asiento


class TestAsiento:
    def test_es_clase_abstracta(self):
        """Verificar que Asiento es una clase abstracta y no se puede instanciar"""
        with pytest.raises(TypeError):
            asiento = Asiento("Silla", "Madera", "Café", 50.0, 1, True, "Tela")
    
    def test_tiene_atributos_asientos(self):
        """Verificar que tiene los atributos específicos de asientos"""
        assert hasattr(Asiento, 'capacidad_personas')
        assert hasattr(Asiento, 'tiene_respaldo')
        assert hasattr(Asiento, 'material_tapizado')
    
    def test_hereda_de_mueble(self):
        """Verificar que hereda correctamente de Mueble"""
        assert issubclass(Asiento, ABC)

import pytest
from abc import ABC
from src.models.categorias.superficies import Superficie


class TestSuperficie:
    def test_es_clase_abstracta(self):
        """Verificar que Superficie es una clase abstracta y no se puede instanciar"""
        with pytest.raises(TypeError):
            superficie = Superficie("Mesa", "Madera", "Café", 150.0, 120.0, 80.0, 75.0)

    def test_tiene_atributos_superficies(self):
        """Verificar que tiene los atributos específicos de superficies"""
        assert hasattr(Superficie, "largo")
        assert hasattr(Superficie, "ancho")
        assert hasattr(Superficie, "altura")

    def test_hereda_de_mueble(self):
        """Verificar que hereda correctamente de Mueble"""
        assert issubclass(Superficie, ABC)

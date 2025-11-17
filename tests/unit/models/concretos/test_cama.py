import pytest
from src.models.concretos.cama import Cama


class TestCama:
    @pytest.fixture
    def cama_basica(self):
        """Fixture para crear una cama básica de prueba"""
        return Cama("Cama Queen", "Madera", "Blanco", 400.0, "queen", False, False)

    def test_instanciacion_correcta(self, cama_basica):
        """Verificar que la cama se instancia correctamente con todos sus atributos"""
        assert cama_basica.nombre == "Cama Queen"
        assert cama_basica.material == "Madera"
        assert cama_basica.color == "Blanco"
        assert cama_basica.precio_base == 400.0
        assert cama_basica.tamaño == "queen"
        assert cama_basica.incluye_colchon == False
        assert cama_basica.tiene_cabecera == False

    def test_calcular_precio(self, cama_basica):
        """Probar el cálculo del precio de la cama"""
        precio = cama_basica.calcular_precio()
        # Precio: 400 + 400 (queen) = 800.0
        assert precio == 800.0
        assert isinstance(precio, float)

    def test_obtener_descripcion(self, cama_basica):
        """Verificar que la descripción contiene la información correcta"""
        descripcion = cama_basica.obtener_descripcion()
        assert "Cama Queen" in descripcion
        assert "Madera" in descripcion
        assert "queen" in descripcion
        assert isinstance(descripcion, str)

    @pytest.mark.parametrize(
        "tamaño,precio_extra",
        [
            ("individual", 0),
            ("matrimonial", 200),
            ("queen", 400),
            ("king", 600),
        ],
    )
    def test_diferentes_tamaños(self, tamaño, precio_extra):
        """Probar camas con diferentes tamaños"""
        precio_base = 400.0
        cama = Cama(
            f"Cama {tamaño}", "Madera", "Blanco", precio_base, tamaño, False, False
        )
        assert cama.tamaño == tamaño
        assert cama.calcular_precio() == precio_base + precio_extra

    def test_cama_con_extras(self):
        """Probar cama con colchón y cabecera"""
        cama = Cama("Cama Completa", "Madera", "Café", 400.0, "king", True, True)
        # Precio: 400 + 600 (king) + 300 (colchón) + 100 (cabecera) = 1400.0
        assert cama.calcular_precio() == 1400.0

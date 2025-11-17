import pytest
from src.models.concretos.mesa import Mesa


class TestMesa:
    @pytest.fixture
    def mesa_basica(self):
        """Fixture para crear una mesa básica de prueba"""
        return Mesa("Mesa Comedor", "Madera", 200.0, "Rectangular", 6)

    def test_instanciacion_correcta(self, mesa_basica):
        """Verificar que la mesa se instancia correctamente con todos sus atributos"""
        # Verificar herencia de atributos de Mueble
        assert mesa_basica.nombre == "Mesa Comedor"
        assert mesa_basica.material == "Madera"
        assert mesa_basica.precio_base == 200.0

        # Verificar atributos específicos de Superficies
        assert mesa_basica.forma == "Rectangular"

        # Verificar atributos específicos de Mesa
        assert mesa_basica.capacidad_personas == 6

    def test_calcular_precio(self, mesa_basica):
        """Probar el cálculo del precio de la mesa"""
        precio = mesa_basica.calcular_precio()
        assert precio == 200.0  # Precio base sin modificaciones
        assert isinstance(precio, float)

    def test_obtener_descripcion(self, mesa_basica):
        """Verificar que la descripción contiene la información correcta"""
        descripcion = mesa_basica.obtener_descripcion()
        assert "Mesa Comedor" in descripcion
        assert "Madera" in descripcion
        assert isinstance(descripcion, str)

    @pytest.mark.parametrize(
        "forma,capacidad",
        [
            ("Rectangular", 6),
            ("Circular", 4),
            ("Ovalada", 8),
            ("Cuadrada", 4),
        ],
    )
    def test_diferentes_formas_y_capacidades(self, forma, capacidad):
        """Probar mesas con diferentes formas y capacidades"""
        mesa = Mesa(f"Mesa {forma}", "Madera", 200.0, forma, capacidad)
        assert mesa.forma == forma
        assert mesa.capacidad_personas == capacidad

    def test_mesa_pequeña(self):
        """Probar mesa con capacidad pequeña"""
        mesa = Mesa("Mesa Pequeña", "Metal", 100.0, "Circular", 2)
        assert mesa.capacidad_personas == 2

    def test_mesa_grande(self):
        """Probar mesa con capacidad grande"""
        mesa = Mesa("Mesa Grande", "Roble", 500.0, "Rectangular", 12)
        assert mesa.capacidad_personas == 12

    def test_mesa_diferentes_materiales(self):
        """Probar mesas con diferentes materiales"""
        mesa_vidrio = Mesa("Mesa Vidrio", "Vidrio", 300.0, "Rectangular", 6)
        mesa_marmol = Mesa("Mesa Mármol", "Mármol", 600.0, "Circular", 4)

        assert mesa_vidrio.material == "Vidrio"
        assert mesa_marmol.material == "Mármol"

    def test_mesa_precio_alto(self):
        """Probar mesa con precio alto"""
        mesa = Mesa("Mesa Premium", "Roble Premium", 1000.0, "Ovalada", 10)
        assert mesa.calcular_precio() == 1000.0

import pytest
from src.models.concretos.escritorio import Escritorio


class TestEscritorio:
    @pytest.fixture
    def escritorio_basico(self):
        """Fixture para crear un escritorio básico de prueba"""
        return Escritorio("Escritorio Oficina", "Madera", 250.0, "Rectangular", 2)

    def test_instanciacion_correcta(self, escritorio_basico):
        """Verificar que el escritorio se instancia correctamente con todos sus atributos"""
        # Verificar herencia de atributos de Mueble
        assert escritorio_basico.nombre == "Escritorio Oficina"
        assert escritorio_basico.material == "Madera"
        assert escritorio_basico.precio_base == 250.0

        # Verificar atributos específicos de Superficies
        assert escritorio_basico.forma == "Rectangular"

        # Verificar atributos específicos de Escritorio
        assert escritorio_basico.numero_cajones == 2

    def test_calcular_precio(self, escritorio_basico):
        """Probar el cálculo del precio del escritorio"""
        precio = escritorio_basico.calcular_precio()
        assert precio == 250.0  # Precio base sin modificaciones
        assert isinstance(precio, float)

    def test_obtener_descripcion(self, escritorio_basico):
        """Verificar que la descripción contiene la información correcta"""
        descripcion = escritorio_basico.obtener_descripcion()
        assert "Escritorio Oficina" in descripcion
        assert "Madera" in descripcion
        assert isinstance(descripcion, str)

    def test_escritorio_sin_cajones(self):
        """Probar escritorio sin cajones"""
        escritorio = Escritorio("Escritorio Simple", "Metal", 150.0, "Rectangular", 0)
        assert escritorio.numero_cajones == 0

    def test_escritorio_muchos_cajones(self):
        """Probar escritorio con muchos cajones"""
        escritorio = Escritorio("Escritorio Ejecutivo", "Roble", 400.0, "L", 6)
        assert escritorio.numero_cajones == 6
        assert escritorio.forma == "L"

    @pytest.mark.parametrize(
        "forma,precio",
        [
            ("Rectangular", 200.0),
            ("L", 300.0),
            ("Circular", 250.0),
            ("Ovalado", 280.0),
        ],
    )
    def test_diferentes_formas(self, forma, precio):
        """Probar escritorios con diferentes formas"""
        escritorio = Escritorio(f"Escritorio {forma}", "Madera", precio, forma, 2)
        assert escritorio.forma == forma
        assert escritorio.calcular_precio() == precio

    def test_escritorio_diferentes_materiales(self):
        """Probar escritorios con diferentes materiales"""
        escritorio_vidrio = Escritorio(
            "Escritorio Vidrio", "Vidrio", 350.0, "Rectangular", 0
        )
        escritorio_metal = Escritorio(
            "Escritorio Metal", "Metal", 200.0, "Rectangular", 3
        )

        assert escritorio_vidrio.material == "Vidrio"
        assert escritorio_metal.material == "Metal"

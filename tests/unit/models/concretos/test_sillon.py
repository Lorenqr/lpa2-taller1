import pytest
from src.models.concretos.sillon import Sillon


class TestSillon:
    @pytest.fixture
    def sillon_basico(self):
        """Fixture para crear un sillón básico de prueba"""
        return Sillon("Sillón Reclinable", "Cuero", 350.0, 4, True)

    def test_instanciacion_correcta(self, sillon_basico):
        """Verificar que el sillón se instancia correctamente con todos sus atributos"""
        # Verificar herencia de atributos de Mueble
        assert sillon_basico.nombre == "Sillón Reclinable"
        assert sillon_basico.material == "Cuero"
        assert sillon_basico.precio_base == 350.0

        # Verificar atributos específicos de Asientos
        assert sillon_basico.numero_patas == 4

        # Verificar atributos específicos de Sillon
        assert sillon_basico.reclinable is True

    def test_calcular_precio(self, sillon_basico):
        """Probar el cálculo del precio del sillón"""
        precio = sillon_basico.calcular_precio()
        assert precio == 350.0  # Precio base sin modificaciones
        assert isinstance(precio, float)

    def test_obtener_descripcion(self, sillon_basico):
        """Verificar que la descripción contiene la información correcta"""
        descripcion = sillon_basico.obtener_descripcion()
        assert "Sillón Reclinable" in descripcion
        assert "Cuero" in descripcion
        assert isinstance(descripcion, str)

    def test_sillon_reclinable(self):
        """Probar sillón con función reclinable"""
        sillon = Sillon("Sillón Comfort", "Tela", 300.0, 4, True)
        assert sillon.reclinable is True

    def test_sillon_no_reclinable(self):
        """Probar sillón sin función reclinable"""
        sillon = Sillon("Sillón Básico", "Tela", 250.0, 4, False)
        assert sillon.reclinable is False

    @pytest.mark.parametrize(
        "material,reclinable,precio",
        [
            ("Cuero", True, 400.0),
            ("Tela", False, 200.0),
            ("Microfibra", True, 350.0),
            ("Vinilo", False, 180.0),
        ],
    )
    def test_diferentes_materiales_y_reclinables(self, material, reclinable, precio):
        """Probar sillones con diferentes materiales y características"""
        sillon = Sillon(f"Sillón {material}", material, precio, 4, reclinable)
        assert sillon.material == material
        assert sillon.reclinable == reclinable
        assert sillon.calcular_precio() == precio

    def test_sillon_sin_patas(self):
        """Probar sillón sin patas (tipo puff)"""
        sillon = Sillon("Sillón Puff", "Tela", 150.0, 0, False)
        assert sillon.numero_patas == 0

    def test_sillon_precio_premium(self):
        """Probar sillón premium con precio alto"""
        sillon = Sillon("Sillón Premium", "Cuero Italiano", 800.0, 4, True)
        assert sillon.calcular_precio() == 800.0

import pytest
from src.models.concretos.sofa import Sofa


class TestSofa:
    @pytest.fixture
    def sofa_basico(self):
        """Fixture para crear un sofá básico de prueba"""
        return Sofa("Sofá Moderno", "Tela", 600.0, 4, 3)

    def test_instanciacion_correcta(self, sofa_basico):
        """Verificar que el sofá se instancia correctamente con todos sus atributos"""
        # Verificar herencia de atributos de Mueble
        assert sofa_basico.nombre == "Sofá Moderno"
        assert sofa_basico.material == "Tela"
        assert sofa_basico.precio_base == 600.0

        # Verificar atributos específicos de Asientos
        assert sofa_basico.numero_patas == 4

        # Verificar atributos específicos de Sofa
        assert sofa_basico.capacidad_personas == 3

    def test_calcular_precio(self, sofa_basico):
        """Probar el cálculo del precio del sofá"""
        precio = sofa_basico.calcular_precio()
        assert precio == 600.0  # Precio base sin modificaciones
        assert isinstance(precio, float)

    def test_obtener_descripcion(self, sofa_basico):
        """Verificar que la descripción contiene la información correcta"""
        descripcion = sofa_basico.obtener_descripcion()
        assert "Sofá Moderno" in descripcion
        assert "Tela" in descripcion
        assert isinstance(descripcion, str)

    @pytest.mark.parametrize(
        "capacidad,precio",
        [
            (2, 450.0),
            (3, 600.0),
            (4, 750.0),
            (5, 900.0),
        ],
    )
    def test_diferentes_capacidades(self, capacidad, precio):
        """Probar sofás con diferentes capacidades"""
        sofa = Sofa(f"Sofá {capacidad} Personas", "Tela", precio, 4, capacidad)
        assert sofa.capacidad_personas == capacidad
        assert sofa.calcular_precio() == precio

    def test_sofa_dos_personas(self):
        """Probar sofá de dos personas (loveseat)"""
        sofa = Sofa("Loveseat", "Cuero", 400.0, 4, 2)
        assert sofa.capacidad_personas == 2

    def test_sofa_sectional(self):
        """Probar sofá seccional grande"""
        sofa = Sofa("Sofá Seccional", "Microfibra", 1200.0, 6, 6)
        assert sofa.capacidad_personas == 6
        assert sofa.numero_patas == 6

    import pytest
from src.models.concretos.sofa import Sofa


class TestSofa:
    @pytest.fixture
    def sofa_basico(self):
        """Fixture para crear un sofá básico de prueba"""
        return Sofa("Sofá Moderno", "Tela", "Gris", 600.0, 3, True, "Tela", True, False, True)
    
    def test_instanciacion_correcta(self, sofa_basico):
        """Verificar que el sofá se instancia correctamente con todos sus atributos"""
        assert sofa_basico.nombre == "Sofá Moderno"
        assert sofa_basico.material == "Tela"
        assert sofa_basico.color == "Gris"
        assert sofa_basico.precio_base == 600.0
        assert sofa_basico.capacidad_personas == 3
        assert sofa_basico.tiene_brazos == True
    
    def test_calcular_precio(self, sofa_basico):
        """Probar el cálculo del precio del sofá"""
        precio = sofa_basico.calcular_precio()
        assert precio > 0
        assert isinstance(precio, float)
    
    def test_obtener_descripcion(self, sofa_basico):
        """Verificar que la descripción contiene la información correcta"""
        descripcion = sofa_basico.obtener_descripcion()
        assert "Sofá Moderno" in descripcion
        assert "Tela" in descripcion
        assert isinstance(descripcion, str)
    
    def test_sofa_dos_personas(self):
        """Probar sofá de dos personas (loveseat)"""
        sofa = Sofa("Loveseat", "Cuero", "Negro", 400.0, 2, True, "Cuero", True, False, False)
        assert sofa.capacidad_personas == 2
    
    def test_sofa_modular(self):
        """Probar sofá modular"""
        sofa = Sofa("Sofá Modular", "Microfibra", "Beige", 800.0, 4, True, "Microfibra", True, True, True)
        assert sofa.es_modular == True

    def test_sofa_sin_patas(self):
        """Probar sofá sin patas visibles"""
        sofa = Sofa("Sofá Bajo", "Tela", 550.0, 0, 3)
        assert sofa.numero_patas == 0

    def test_sofa_precio_economico(self):
        """Probar sofá económico"""
        sofa = Sofa("Sofá Económico", "Tela", 300.0, 4, 2)
        assert sofa.calcular_precio() == 300.0

    def test_sofa_precio_premium(self):
        """Probar sofá premium"""
        sofa = Sofa("Sofá Premium", "Cuero Italiano", 1500.0, 4, 4)
        assert sofa.calcular_precio() == 1500.0

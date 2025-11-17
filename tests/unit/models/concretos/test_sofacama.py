import pytest
from src.models.concretos.sofacama import SofaCama


class TestSofaCama:
    @pytest.fixture
    def sofacama_basico(self):
        """Fixture para crear un sofá cama básico de prueba"""
        return SofaCama("Sofá Cama Moderno", "Tela", 500.0, 3, "Queen")

    def test_instanciacion_correcta(self, sofacama_basico):
        """Verificar que el sofá cama se instancia correctamente con todos sus atributos"""
        # Verificar herencia de atributos de Mueble
        assert sofacama_basico.nombre == "Sofá Cama Moderno"
        assert sofacama_basico.material == "Tela"
        assert sofacama_basico.precio_base == 500.0

        # Verificar atributos de Sofa
        assert sofacama_basico.capacidad_personas == 3

        # Verificar atributos de Cama
        assert sofacama_basico.tamaño_colchon == "Queen"

    def test_herencia_multiple(self):
        """Verificar la herencia múltiple del sofá cama"""
        sofa_cama = SofaCama("Sofá Cama Moderno", "Tela", 500.0, 3, "Queen")

        # Verificar atributos de Sofa
        assert sofa_cama.capacidad_personas == 3

        # Verificar atributos de Cama
        assert sofa_cama.tamaño_colchon == "Queen"

        # Verificar método específico si existe
        assert hasattr(sofa_cama, "calcular_precio")
        assert hasattr(sofa_cama, "obtener_descripcion")

    def test_calcular_precio(self, sofacama_basico):
        """Probar el cálculo del precio del sofá cama"""
        precio = sofacama_basico.calcular_precio()
        # Puede incluir recargos de ambas clases si está implementado
        assert precio >= 500.0
        assert isinstance(precio, float)

    def test_obtener_descripcion(self, sofacama_basico):
        """Verificar que la descripción contiene la información correcta"""
        descripcion = sofacama_basico.obtener_descripcion()
        assert "Sofá Cama Moderno" in descripcion
        assert "Tela" in descripcion
        assert isinstance(descripcion, str)

    def test_resolucion_metodos(self):
        """Verificar la resolución de métodos (MRO - Method Resolution Order)"""
        sofa_cama = SofaCama("Sofá Cama", "Cuero", 600.0, 2, "Full")

        # Verificar que usa el método correcto según MRO
        precio = sofa_cama.calcular_precio()
        assert precio >= 600.0

    @pytest.mark.parametrize(
        "capacidad,tamaño,precio",
        [
            (2, "Individual", 400.0),
            (3, "Full", 550.0),
            (3, "Queen", 650.0),
            (4, "King", 800.0),
        ],
    )
    def test_diferentes_configuraciones(self, capacidad, tamaño, precio):
        """Probar sofás cama con diferentes configuraciones"""
        sofa_cama = SofaCama(f"Sofá Cama {tamaño}", "Tela", precio, capacidad, tamaño)
        assert sofa_cama.capacidad_personas == capacidad
        assert sofa_cama.tamaño_colchon == tamaño
        assert sofa_cama.calcular_precio() >= precio

    def test_sofacama_dos_personas(self):
        """Probar sofá cama pequeño para dos personas"""
        sofa_cama = SofaCama("Sofá Cama Compacto", "Tela", 450.0, 2, "Full")
        assert sofa_cama.capacidad_personas == 2
        assert sofa_cama.tamaño_colchon == "Full"

    def test_sofacama_premium(self):
        """Probar sofá cama premium con características superiores"""
        sofa_cama = SofaCama("Sofá Cama Premium", "Cuero", 1000.0, 4, "King")
        assert sofa_cama.capacidad_personas == 4
        assert sofa_cama.tamaño_colchon == "King"
        assert sofa_cama.material == "Cuero"

    @pytest.mark.parametrize(
        "material,precio",
        [
            ("Tela", 500.0),
            ("Cuero", 700.0),
            ("Microfibra", 550.0),
            ("Terciopelo", 650.0),
        ],
    )
    def test_diferentes_materiales(self, material, precio):
        """Probar sofás cama con diferentes materiales"""
        sofa_cama = SofaCama(f"Sofá Cama {material}", material, precio, 3, "Queen")
        assert sofa_cama.material == material
        assert sofa_cama.calcular_precio() >= precio

    def test_sofacama_economico(self):
        """Probar sofá cama económico"""
        sofa_cama = SofaCama("Sofá Cama Económico", "Tela", 350.0, 2, "Individual")
        assert sofa_cama.calcular_precio() >= 350.0

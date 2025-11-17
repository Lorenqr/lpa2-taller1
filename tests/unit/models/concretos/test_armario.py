import pytest
from src.models.concretos.armario import Armario


class TestArmario:
    @pytest.fixture
    def armario_basico(self):
        """Fixture para crear un armario básico de prueba"""
        return Armario("Armario Clásico", "Madera", "Café", 300, 2, 2, False)
    
    def test_instanciacion_correcta(self, armario_basico):
        """Verificar que el armario se instancia correctamente con todos sus atributos"""
        # Verificar atributos
        assert armario_basico.nombre == "Armario Clásico"
        assert armario_basico.material == "Madera"
        assert armario_basico.color == "Café"
        assert armario_basico.precio_base == 300
        
        # Verificar atributos específicos de Armario
        assert armario_basico.num_puertas == 2
        assert armario_basico.num_cajones == 2
        assert armario_basico.tiene_espejos == False
    
    def test_calcular_precio(self, armario_basico):
        """Probar el cálculo del precio del armario"""
        precio = armario_basico.calcular_precio()
        # Precio base 300 + (2 puertas * 50) + (2 cajones * 30) = 460
        assert precio == 460
        assert isinstance(precio, int)
    
    def test_obtener_descripcion(self, armario_basico):
        """Verificar que la descripción contiene la información correcta"""
        descripcion = armario_basico.obtener_descripcion()
        assert "Armario Clásico" in descripcion
        assert "Madera" in descripcion
        assert isinstance(descripcion, str)
    
    def test_armario_sin_cajones(self):
        """Probar armario sin cajones"""
        armario = Armario("Armario Simple", "Metal", "Gris", 250, 2, 0, False)
        assert armario.num_cajones == 0
        assert armario.num_puertas == 2
    
    def test_armario_con_espejos(self):
        """Probar armario con espejos"""
        armario = Armario("Armario con Espejos", "Madera", "Blanco", 400, 3, 0, True)
        # Precio: 400 + (3*50) + 100 (espejos) = 650
        assert armario.calcular_precio() == 650
        assert armario.tiene_espejos == True
    
    def test_armario_grande(self):
        """Probar armario grande con muchas puertas y cajones"""
        armario = Armario("Armario Grande", "Roble", "Natural", 500, 4, 6, True)
        # Precio: 500 + (4*50) + (6*30) + 100 = 980
        assert armario.calcular_precio() == 980

import pytest
from src.models.composicion.comedor import Comedor
from src.models.concretos.mesa import Mesa
from src.models.concretos.silla import Silla


class TestComedorComposicion:
    @pytest.fixture
    def mesa_basica(self):
        """Fixture para crear una mesa básica de prueba"""
        return Mesa("Mesa Roble", "Roble", "Natural", 300.0, "rectangular", 150.0, 90.0, 75.0, 8)

    @pytest.fixture
    def sillas_basicas(self):
        """Fixture para crear un conjunto de sillas básicas"""
        return [Silla("Silla Roble", "Roble", "Natural", 80.0, True, "Tela") for _ in range(8)]

    @pytest.fixture
    def comedor_completo(self, mesa_basica, sillas_basicas):
        """Fixture para crear un comedor completo con mesa y sillas"""
        return Comedor("Comedor Familiar", mesa_basica, sillas_basicas)

    @pytest.fixture
    def comedor_vacio(self, mesa_basica):
        """Fixture para crear un comedor sin sillas"""
        return Comedor("Comedor Simple", mesa_basica)

    def test_composicion_correcta(self, comedor_completo):
        """Verificar que la composición funciona correctamente"""
        assert comedor_completo.mesa is not None
        assert len(comedor_completo.sillas) == 8
        assert isinstance(comedor_completo.mesa, Mesa)
        assert all(isinstance(silla, Silla) for silla in comedor_completo.sillas)

    def test_instanciacion_con_nombre(self, comedor_completo):
        """Verificar que el comedor se instancia con nombre correcto"""
        assert comedor_completo.nombre == "Comedor Familiar"

    def test_calcular_precio_total(self, comedor_completo):
        """Probar el cálculo del precio total del comedor"""
        precio_total = comedor_completo.calcular_precio()
        # El precio no será exacto por los recargos de las clases
        assert precio_total > 300.0  # Al menos el precio base de la mesa

    def test_calcular_precio_solo_mesa(self, comedor_vacio):
        """Probar el cálculo del precio de un comedor sin sillas"""
        precio_total = comedor_vacio.calcular_precio()
        assert precio_total > 0  # Debe tener el precio de la mesa

    def test_agregar_silla(self, comedor_vacio):
        """Probar agregar sillas al comedor"""
        silla_nueva = Silla("Silla Nueva", "Roble", "Natural", 80.0, True, "Tela")
        comedor_vacio.agregar_silla(silla_nueva)

        assert len(comedor_vacio.sillas) == 1
        assert comedor_vacio.sillas[0] == silla_nueva

    def test_agregar_multiples_sillas(self, comedor_vacio):
        """Probar agregar múltiples sillas"""
        for i in range(6):
            silla = Silla(f"Silla {i + 1}", "Roble", "Natural", 80.0, True, "Tela")
            comedor_vacio.agregar_silla(silla)

        assert len(comedor_vacio.sillas) == 6

    def test_quitar_silla(self, comedor_completo):
        """Probar quitar una silla del comedor"""
        silla_a_quitar = comedor_completo.sillas[0]
        comedor_completo.quitar_silla(silla_a_quitar)

        assert len(comedor_completo.sillas) == 7

    def test_obtener_descripcion(self, comedor_completo):
        """Verificar que la descripción del comedor es correcta"""
        descripcion = comedor_completo.obtener_descripcion()

        assert "Comedor Familiar" in descripcion
        assert "Mesa Roble" in descripcion
        assert isinstance(descripcion, str)

    def test_cantidad_sillas(self, comedor_completo):
        """Verificar el método cantidad_sillas si existe"""
        if hasattr(comedor_completo, "cantidad_sillas"):
            assert comedor_completo.cantidad_sillas() == 8
        else:
            assert len(comedor_completo.sillas) == 8

    def test_comedor_diferente_numero_sillas(self):
        """Probar comedor con diferente número de sillas"""
        mesa = Mesa("Mesa Pequeña", "Pino", "Natural", 150.0, "redonda", 90.0, 90.0, 75.0, 4)
        sillas = [Silla("Silla Pino", "Pino", "Natural", 50.0, True, "Tela") for _ in range(4)]
        comedor = Comedor("Comedor Pequeño", mesa, sillas)

        assert len(comedor.sillas) == 4
        assert comedor.calcular_precio() > 150.0  # Al menos el precio base de la mesa

    def test_independencia_objetos(self, mesa_basica, sillas_basicas):
        """Verificar que los objetos pueden existir independientemente"""
        # Verificar que la mesa y las sillas pueden existir sin el comedor
        assert mesa_basica.calcular_precio() > 0
        assert all(silla.calcular_precio() > 0 for silla in sillas_basicas)

        # Crear comedor y verificar que no afecta los objetos originales
        comedor = Comedor("Test", mesa_basica, sillas_basicas)
        assert comedor.mesa.nombre == "Mesa Roble"
        assert len(comedor.sillas) == 8

    def test_comedor_sin_sillas_iniciales(self, comedor_vacio):
        """Verificar que se puede crear un comedor sin sillas"""
        assert len(comedor_vacio.sillas) == 0
        assert comedor_vacio.mesa is not None

    @pytest.mark.parametrize(
        "num_sillas,precio_silla",
        [
            (4, 50.0),
            (6, 75.0),
            (8, 80.0),
            (10, 100.0),
        ],
    )
    def test_diferentes_configuraciones(self, num_sillas, precio_silla):
        """Probar comedores con diferentes configuraciones"""
        mesa = Mesa("Mesa Test", "Madera", "Natural", 200.0, "rectangular", 120.0, 80.0, 75.0, num_sillas)
        sillas = [
            Silla(f"Silla {i}", "Madera", "Natural", precio_silla, True, "Tela")
            for i in range(num_sillas)
        ]
        comedor = Comedor("Comedor Test", mesa, sillas)

        assert comedor.calcular_precio() > 200.0  # Al menos el precio base de la mesa

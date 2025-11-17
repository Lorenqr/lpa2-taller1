import pytest
from src.models.concretos.comedor import Comedor
from src.models.concretos.mesa import Mesa
from src.models.concretos.silla import Silla


class TestComedorConcreto:
    @pytest.fixture
    def mesa_basica(self):
        """Fixture para crear una mesa básica de prueba"""
        return Mesa("Mesa Comedor", "Roble", 200.0, "Rectangular", 6)

    @pytest.fixture
    def silla_basica(self):
        """Fixture para crear una silla básica de prueba"""
        return Silla("Silla Comedor", "Roble", 50.0, 4, "Roble")

    @pytest.fixture
    def comedor_basico(self, mesa_basica):
        """Fixture para crear un comedor básico de prueba"""
        return Comedor(mesa_basica)

    @pytest.fixture
    def comedor_completo(self, mesa_basica, silla_basica):
        """Fixture para crear un comedor completo con sillas"""
        sillas = [Silla("Silla Comedor", "Roble", 50.0, 4, "Roble") for _ in range(6)]
        return Comedor(mesa_basica, sillas)

    def test_instanciacion_correcta(self, comedor_basico, mesa_basica):
        """Verificar que el comedor se instancia correctamente"""
        assert comedor_basico.mesa is not None
        assert isinstance(comedor_basico.mesa, Mesa)
        assert comedor_basico.mesa == mesa_basica
        assert isinstance(comedor_basico.sillas, list)
        assert len(comedor_basico.sillas) == 0

    def test_comedor_con_sillas(self, comedor_completo):
        """Verificar comedor con sillas en la inicialización"""
        assert len(comedor_completo.sillas) == 6
        assert all(isinstance(silla, Silla) for silla in comedor_completo.sillas)

    def test_agregar_silla(self, comedor_basico, silla_basica):
        """Probar agregar sillas al comedor"""
        assert len(comedor_basico.sillas) == 0
        comedor_basico.agregar_silla(silla_basica)
        assert len(comedor_basico.sillas) == 1
        assert comedor_basico.sillas[0] == silla_basica

    def test_quitar_silla(self, comedor_completo):
        """Probar quitar sillas del comedor"""
        silla_a_quitar = comedor_completo.sillas[0]
        cantidad_inicial = len(comedor_completo.sillas)

        comedor_completo.quitar_silla(silla_a_quitar)
        assert len(comedor_completo.sillas) == cantidad_inicial - 1
        assert silla_a_quitar not in comedor_completo.sillas

    def test_quitar_silla_no_existente(self, comedor_completo):
        """Probar quitar una silla que no existe"""
        silla_nueva = Silla("Silla Nueva", "Pino", 40.0, 4, "Pino")
        cantidad_inicial = len(comedor_completo.sillas)

        comedor_completo.quitar_silla(silla_nueva)
        assert len(comedor_completo.sillas) == cantidad_inicial

    def test_cantidad_sillas(self, comedor_completo):
        """Probar el método cantidad_sillas"""
        assert comedor_completo.cantidad_sillas() == 6

    def test_calcular_precio_total(self, comedor_completo):
        """Probar el cálculo del precio total del comedor"""
        precio_total = comedor_completo.calcular_precio_total()
        precio_esperado = 200.0 + (6 * 50.0)  # Mesa + 6 sillas
        assert precio_total == precio_esperado

    def test_calcular_precio_solo_mesa(self, comedor_basico):
        """Probar el precio de un comedor sin sillas"""
        precio_total = comedor_basico.calcular_precio_total()
        assert precio_total == 200.0

    def test_descripcion(self, comedor_completo):
        """Verificar que la descripción contiene la información correcta"""
        descripcion = comedor_completo.descripcion()
        assert "Comedor con mesa" in descripcion
        assert "6 sillas" in descripcion
        assert isinstance(descripcion, str)

    def test_comedor_vacio_descripcion(self, comedor_basico):
        """Verificar descripción de comedor sin sillas"""
        descripcion = comedor_basico.descripcion()
        assert "0 sillas" in descripcion

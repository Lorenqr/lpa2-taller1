"""
Clase concreta Sofa.
Implementa un mueble de asiento para varias personas.
"""

from ..categorias.asientos import Asiento


class Sofa(Asiento):
    """
    Clase concreta que representa un sofá.

    Hereda de Asiento y añade características específicas como:
    - Brazos
    - Diseño modular
    - Cojines incluidos
    """

    def __init__(
        self,
        nombre: str,
        material: str,
        color: str,
        precio_base: float,
        capacidad_personas: int = 3,
        tiene_respaldo: bool = True,
        material_tapizado: str | None = None,
        tiene_brazos: bool = True,
        es_modular: bool = False,
        incluye_cojines: bool = False,
    ):
        super().__init__(
            nombre,
            material,
            color,
            precio_base,
            capacidad_personas,
            tiene_respaldo,
            material_tapizado,
        )

        self._tiene_brazos = bool(tiene_brazos)
        self._es_modular = bool(es_modular)
        self._incluye_cojines = bool(incluye_cojines)



    @property
    def tiene_brazos(self) -> bool:
        """Indica si el sofá posee brazos laterales."""
        return self._tiene_brazos

    @property
    def es_modular(self) -> bool:
        """Indica si es un sofá modular (secciones independientes)."""
        return self._es_modular

    @property
    def incluye_cojines(self) -> bool:
        """Indica si el sofá incluye cojines adicionales."""
        return self._incluye_cojines


    def calcular_precio(self) -> float:
        """
        Calcula el precio final del sofá.

        Reglas:
        - Se multiplica por el factor de comodidad del asiento base.
        - +150 si tiene brazos.
        - +200 si es modular.
        - +50 si incluye cojines.
        """
        precio = self.precio_base

        # Aplicar factor de comodidad heredado
        precio *= self.calcular_factor_comodidad()

        # Extras del sofá
        if self.tiene_brazos:
            precio += 150
        if self.es_modular:
            precio += 200
        if self.incluye_cojines:
            precio += 50

        return round(precio, 2)



    def obtener_descripcion(self) -> str:
        """
        Retorna una descripción detallada del sofá.
        """
        desc = (
            f"Sofá '{self.nombre}'\n"
            f"  Material: {self.material}\n"
            f"  Color: {self.color}\n"
            f"  {self.obtener_info_asiento()}\n"
            f"  Brazos: {'Sí' if self.tiene_brazos else 'No'}\n"
            f"  Modular: {'Sí' if self.es_modular else 'No'}\n"
            f"  Incluye cojines: {'Sí' if self.incluye_cojines else 'No'}\n"
            f"  Precio final: ${self.calcular_precio()}"
        )
        return desc


    def __str__(self) -> str:
        return f"Sofá {self.nombre} ({self.capacidad_personas} personas)"

    def __repr__(self) -> str:
        return (
            f"Sofa(nombre={self.nombre!r}, material={self.material!r}, "
            f"color={self.color!r}, precio_base={self.precio_base!r}, "
            f"capacidad_personas={self.capacidad_personas!r}, "
            f"tiene_respaldo={self.tiene_respaldo!r}, "
            f"material_tapizado={self.material_tapizado!r}, "
            f"tiene_brazos={self.tiene_brazos!r}, "
            f"es_modular={self.es_modular!r}, "
            f"incluye_cojines={self.incluye_cojines!r})"
        )

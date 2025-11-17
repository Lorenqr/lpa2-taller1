"""
Clase SofaCama que implementa herencia múltiple.
Esta clase hereda tanto de Sofa como de Cama.
"""

from .sofa import Sofa
from .cama import Cama


class SofaCama(Sofa, Cama):
    """
    Clase que implementa herencia múltiple heredando de Sofa y Cama.

    Un sofá-cama funciona como sofá durante el día
    y como cama durante la noche.
    """

    def __init__(
        self,
        nombre: str,
        material: str,
        color: str,
        precio_base: int,
        capacidad_personas: int = 3,
        material_tapizado: str = "tela",
        tamaño_cama: str = "matrimonial",
        incluye_colchon: bool = True,
        mecanismo_conversion: str = "plegable",
    ):
        """
        Constructor del sofá cama.
        """
        
        Sofa.__init__(
            self,
            nombre,
            material,
            color,
            precio_base,
            capacidad_personas,
            True,  # sofá cama siempre tiene espaldar
            material_tapizado,
        )

        # Atributos específicos de cama
        self._tamaño = tamaño_cama

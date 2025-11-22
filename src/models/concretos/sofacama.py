from typing import Any, Optional, Iterable
from .sofa import Sofa


class SofaCama(Sofa):
    """
    SofaCama flexible que extrae precio, patas y tamaño del colchón de la lista de arguments
    que usan los tests. Reutiliza la lógica de Sofa para interpretar color/precio/patas/capacidad.
    Además intenta detectar el tamaño de colchón si aparece en los args posicionales.
    """

    _TAMANOS = {"individual", "matrimonial", "queen", "king"}

    def __init__(self, *args: Any, **kwargs: Any):
        # Extraer tamano_colchon si aparece explícitamente en kwargs
        tamano_colchon: Optional[str] = None
        if "tamano_colchon" in kwargs:
            tamano_colchon = kwargs.pop("tamano_colchon")

        # Convertir args a lista para inspeccionar
        args_list = list(args)

        # Intentar detectar tamano_colchon posicional (un string que coincide con _TAMANOS)
        for a in args_list[:]:
            if isinstance(a, str) and a.lower() in self._TAMANOS:
                tamano_colchon = a
                # No eliminar el argumento de la lista porque Sofa puede usar strings previos como color
                break

        # Delegar parsing complejo de precio/color/patas/capacidad a Sofa.
        # Llamamos a super con los mismos args y kwargs (Sofa interpreta).
        super().__init__(*args, **kwargs)

        # Asignar atributo de sofá-cama
        self.tamano_colchon = tamano_colchon
        # Si no se encontró tamano_colchon y se pasó un string posicional que queda
        # después del precio en args, intentar asignarlo como tamano (fallback).
        if self.tamano_colchon is None:
            # Buscar en args el primer string después del precio posicional (heurística)
            index_precio = None
            for i, a in enumerate(args_list):
                if isinstance(a, (int, float)):
                    index_precio = i
                    break
            if index_precio is not None:
                # revisar elementos posicionales posteriores en busca de un tamaño
                for b in args_list[index_precio + 1 :]:
                    if isinstance(b, str) and b.lower() in self._TAMANOS:
                        self.tamano_colchon = b
                        break

    def obtener_descripcion(self) -> str:
        base = super().obtener_descripcion()
        tam = f" - Tipo cama: {self.tamano_colchon}" if getattr(self, "tamano_colchon", None) else ""
        return f"{base}{tam}"
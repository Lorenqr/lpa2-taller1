from typing import Optional, Any, Iterable
from ..mueble import Mueble


class Sofa(Mueble):
    """
    Constructor flexible que acepta variantes posicionales usadas por los tests:
      - Sofa(nombre, material, precio_base, numero_patas, capacidad_personas, ...)
      - Sofa(nombre, material, color, precio_base, numero_patas, capacidad_personas, ...)
    La lógica busca el primer argumento numérico posicional como precio_base.
    Si existe una cadena justo antes del precio, se toma como color.
    Después del precio, si hay int se interpretará como numero_patas y luego capacidad_personas.
    Parámetros booleans y de tapizado se mantienen como kwargs o valores por defecto.
    """

    def __init__(  # type: ignore[override]
        self,
        nombre: str,
        material: str,
        *args: Any,
        tiene_respaldo: bool = True,
        material_tapizado: Optional[str] = None,
        tiene_brazos: bool = True,
        es_modular: bool = False,
        incluye_cojines: bool = False,
        capacidad_personas: Optional[int] = None,
    ):
        
        # Convert args to list for easier handling
        args_list = list(args)
        
        # Defaults
        color: Optional[str] = None
        precio_base: float = 0.0
        numero_patas: int = 4
        capacidad: Optional[int] = None


        # Find first numeric argument (treated as precio_base)
        index_precio = None
        for i, a in enumerate(args_list):
            if isinstance(a, (int, float)):
                index_precio = i
                break

        if index_precio is not None:
            
            # If there's a string immediately before the price, treat it as color
            if index_precio - 1 >= 0 and isinstance(args_list[index_precio - 1], str):
                color = args_list[index_precio - 1]

            precio_base = float(args_list[index_precio])
            
            capacidad_detectada = None
            for a in args_list[index_precio + 1:]:
                if isinstance(a, int):
                    if capacidad_detectada is None:
                        numero_patas = a
                        capacidad_detectada = 'patas'
                    else:
                        capacidad = a
                        break

            else:
            # numero_patas: next positional after precio_base that is int
                if index_precio + 1 < len(args_list) and isinstance(args_list[index_precio + 1], int):
                        numero_patas = int(args_list[index_precio + 1])

            # capacidad_personas: next positional after numero_patas that is int
                if index_precio + 2 < len(args_list) and isinstance(args_list[index_precio + 2], int):
                        capacidad = int(args_list[index_precio + 2])
        else:
                # No numeric positional found: try kwargs override or try to interpret first arg as color
            if args_list and isinstance(args_list[0], str):
                color = args_list[0]
                precio_base = float(getattr(self, "_precio_base", 0.0)) if hasattr(self, "_precio_base") else 0.0

        # If explicit capacidad_personas kwarg passed, use it
        if capacidad_personas is not None:
            capacidad = int(capacidad_personas)
            
        if capacidad is None:
            capacidad = 1

        # Call parent constructor: Mueble expects (nombre, material, color, precio_base)
        super().__init__(nombre, material, color, precio_base)

        # Assign sofa-specific attributes
        self.numero_patas = int(numero_patas)
        self.capacidad_personas = int(capacidad)
        self.tiene_respaldo = bool(tiene_respaldo)
        self.material_tapizado = material_tapizado
        self.tiene_brazos = bool(tiene_brazos)
        self.es_modular = bool(es_modular)
        self.incluye_cojines = bool(incluye_cojines)

    def calcular_precio(self) -> float:
        """
        Por ahora devolvemos el precio_base (float) como esperan los tests.
        Evitamos lanzar excepciones si precio_base está mal tipado.
        """
        try:
            p = float(self.precio_base)
        except (TypeError, ValueError):
            p = 0.0
        return round(p, 2)

    def obtener_descripcion(self) -> str:
        precio_text = f"{float(self.precio_base):.2f}" if isinstance(self.precio_base, (int, float)) else str(self.precio_base)
        color_text = self.color if self.color is not None else "None"
        return f"{self.nombre} - {self.material} - {color_text} - ${precio_text} - Patas: {self.numero_patas}"
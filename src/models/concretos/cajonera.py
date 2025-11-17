"""
Clase concreta Cajonera.
Representa una cajonera genérica utilizada en el mobiliario.
"""


class Cajonera:
    """
    Clase concreta que representa una cajonera.

    Atributos:
        nombre (str): Nombre del modelo de la cajonera.
        material (str): Material principal de construcción.
        color (str): Color exterior.
        precio_base (int): Precio inicial sin añadidos.
        num_cajones (int): Cantidad de cajones que contiene.
        tiene_ruedas (bool): Indica si incluye ruedas.
    """

    def __init__(
        self,
        nombre: str,
        material: str,
        color: str,
        precio_base: int,
        num_cajones: int = 3,
        tiene_ruedas: bool = False,
    ):
        self.nombre = nombre
        self.material = material
        self.color = color
        self.precio_base = int(precio_base) if precio_base is not None else 0

        # Validación ligera y segura
        self.num_cajones = max(0, int(num_cajones))
        self.tiene_ruedas = bool(tiene_ruedas)


    def calcular_precio(self) -> int:
        """
        Calcula el precio final de la cajonera.

        Reglas:
            - Cada cajón agrega +20 al precio.
            - Si tiene ruedas, agrega +30 al precio total.
        """
        precio = self.precio_base
        precio += self.num_cajones * 20

        if self.tiene_ruedas:
            precio += 30

        return int(round(precio))

    def obtener_descripcion(self) -> str:
        """
        Retorna una descripción detallada de la cajonera.
        """
        return (
            f"Cajonera '{self.nombre}': Material={self.material}, Color={self.color}, "
            f"Cajones={self.num_cajones}, Ruedas={'Sí' if self.tiene_ruedas else 'No'}, "
            f"Precio base=${self.precio_base}"
        )


    def __str__(self) -> str:
        return f"Cajonera {self.nombre} ({self.num_cajones} cajones)"

    def __repr__(self) -> str:
        return (
            f"Cajonera(nombre={self.nombre!r}, material={self.material!r}, "
            f"color={self.color!r}, precio_base={self.precio_base!r}, "
            f"num_cajones={self.num_cajones!r}, tiene_ruedas={self.tiene_ruedas!r})"
        )

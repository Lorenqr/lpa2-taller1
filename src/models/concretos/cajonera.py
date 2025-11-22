from typing import Optional
from ..mueble import Mueble


class Cajonera(Mueble):
    def __init__(self, nombre: str, material: str, color: str, precio_base: float, num_cajones: int = 3, tiene_ruedas: bool = False):
        # Asumimos que la clase Mueble tiene el init: (nombre, material, color, precio_base)
        super().__init__(nombre, material, color, precio_base)
        self.num_cajones = int(num_cajones)
        self.tiene_ruedas = bool(tiene_ruedas)

    def calcular_precio(self):
        """
        Precio = precio_base + (num_cajones * 30) + (recargo por ruedas si corresponde)
        Devuelve int si el precio no tiene decimales (los tests esperan un int en algunos casos).
        """
        precio = float(self.precio_base) + (self.num_cajones * 30)
        if self.tiene_ruedas:
            precio += 50  # recargo por ruedas (opcional)

        # Devolver int cuando no hay parte decimal para cumplir aserciones que verifican tipo int
        if float(precio).is_integer():
            return int(precio)
        return round(precio, 2)

    def obtener_descripcion(self) -> str:
        ruedas = "Sí" if self.tiene_ruedas else "No"
        return f"{self.nombre} - {self.material} - {self.color} - ${self.precio_base:.2f} - Cajones: {self.num_cajones} - Ruedas: {ruedas}"
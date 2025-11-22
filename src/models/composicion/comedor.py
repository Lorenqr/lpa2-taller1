"""
Clase Comedor que implementa composición.
Un comedor está compuesto por una mesa y varias sillas.
"""

from typing import List, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..concretos.mesa import Mesa
    from ..concretos.silla import Silla


class Comedor:
    """
    Clase que implementa la composición de una mesa y varias sillas.

    Conceptos OOP:
    - Composición: El comedor contiene otros objetos (mesa y sillas).
    - Agregación: Mesa y sillas pueden existir fuera del comedor.
    - Encapsulación: Los atributos no se exponen directamente.
    - Abstracción: Facilita la gestión del conjunto.
    """

    def __init__(self, nombre: str, mesa: "Mesa", sillas: List["Silla"] | None = None):
        """
        Inicializa un comedor compuesto por una mesa y un conjunto opcional de sillas.
        """
        self._nombre = nombre
        self._mesa = mesa
        self._sillas: List["Silla"] = sillas.copy() if sillas else []

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def mesa(self) -> "Mesa":
        return self._mesa

    @property
    def sillas(self) -> List["Silla"]:
        return self._sillas.copy()

    def agregar_silla(self, silla: "Silla") -> str:
        """
        Agrega una silla al comedor si hay espacio disponible.
        """

        # Validar que el tipo sea correcto
        from ..concretos.silla import Silla as ClaseSilla

        if not isinstance(silla, ClaseSilla):
            return "Error: Solo se pueden agregar objetos de tipo Silla."

        # Validar capacidad máxima
        capacidad_maxima = self._calcular_capacidad_maxima()
        if len(self._sillas) >= capacidad_maxima:
            return f"No se pueden agregar más sillas. Capacidad máxima: {capacidad_maxima}."

        self._sillas.append(silla)
        return f"Silla '{getattr(silla, 'nombre', 'Sin nombre')}' agregada exitosamente."

    def quitar_silla(self, indice: Union[int, "Silla"] = -1) -> str:
        """
        Quita una silla por índice (por defecto la última) o por instancia.
        Si se pasa una instancia de Silla, se intenta remover esa instancia.
        """
        if not self._sillas:
            return "No hay sillas para quitar."

        from ..concretos.silla import Silla as ClaseSilla

        # quitar por objeto
        if isinstance(indice, ClaseSilla):
            try:
                self._sillas.remove(indice)
                return f"Silla '{getattr(indice, 'nombre', 'Sin nombre')}' removida del comedor."
            except ValueError:
                return "La silla indicada no se encuentra en el comedor."

        # quitar por índice (espera int)
        try:
            silla_removida = self._sillas.pop(int(indice))
        except (IndexError, ValueError, TypeError):
            return "Índice de silla inválido."

        return f"Silla '{getattr(silla_removida, 'nombre', 'Sin nombre')}' removida del comedor."

    # Método esperado por los tests: calcular_precio()
    def calcular_precio(self) -> float:
        return self.calcular_precio_total()

    def calcular_precio_total(self) -> float:
        """
        Suma el precio de la mesa y todas las sillas.
        Si hay 4 o más sillas, aplica un 5% de descuento.
        """
        precio_total = self._mesa.calcular_precio()
        precio_total += sum(silla.calcular_precio() for silla in self._sillas)

        if len(self._sillas) >= 4:
            precio_total *= 0.95  # descuento 5%

        return round(precio_total, 2)

    # Método esperado por los tests: obtener_descripcion()
    def obtener_descripcion(self) -> str:
        return self.obtener_descripcion_completa()

    def obtener_descripcion_completa(self) -> str:
        """
        Retorna una descripción detallada del comedor.
        Se cambia el encabezado para mostrar el nombre tal cual (sin forzar mayúsculas),
        así los tests que buscan "Comedor Familiar" lo encontrarán.
        """
        descripcion = f"=== {self.nombre} ===\n\n"

        descripcion += "MESA:\n"
        descripcion += self._mesa.obtener_descripcion() + "\n\n"

        if self._sillas:
            descripcion += f"SILLAS ({len(self._sillas)} unidades):\n"
            for i, silla in enumerate(self._sillas, 1):
                descripcion += f"{i}. {silla.obtener_descripcion()}\n"
        else:
            descripcion += "SILLAS: Ninguna incluida\n"

        descripcion += f"\n--- PRECIO TOTAL: ${self.calcular_precio_total():.2f} ---"
        if len(self._sillas) >= 4:
            descripcion += "\n(Incluye 5% de descuento por set completo)"

        return descripcion

    def obtener_resumen(self) -> dict:
        """
        Devuelve un resumen estadístico del comedor.
        """
        return {
            "nombre": self.nombre,
            "total_muebles": 1 + len(self._sillas),
            "precio_mesa": self._mesa.calcular_precio(),
            "precio_sillas": sum(silla.calcular_precio() for silla in self._sillas),
            "precio_total": self.calcular_precio_total(),
            "capacidad_personas": len(self._sillas),
            "materiales_utilizados": self._obtener_materiales_unicos(),
        }

    def _obtener_materiales_unicos(self) -> list:
        """
        Obtiene la lista de materiales únicos utilizados.
        """
        materiales = set()

        if hasattr(self._mesa, "material"):
            materiales.add(self._mesa.material)

        for silla in self._sillas:
            if hasattr(silla, "material"):
                materiales.add(silla.material)

            if hasattr(silla, "material_tapizado") and silla.material_tapizado:
                materiales.add(silla.material_tapizado)

        return list(materiales)

    def _calcular_capacidad_maxima(self) -> int:
        """
        Calcula la capacidad máxima de sillas basada en atributos de la mesa.
        """
        return getattr(self._mesa, "capacidad_personas", 6)

    def __str__(self) -> str:
        return f"Comedor {self._nombre}: Mesa + {len(self._sillas)} sillas"

    def __len__(self) -> int:
        return 1 + len(self._sillas)
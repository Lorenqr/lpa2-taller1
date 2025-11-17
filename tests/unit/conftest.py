"""
Configuración compartida para todas las pruebas unitarias.
Este archivo contiene fixtures y configuraciones globales para pytest.
"""

import pytest
import sys
from pathlib import Path

# Agregar el directorio raíz al path de Python
root_dir = Path(__file__).parent.parent.parent
sys.path.insert(0, str(root_dir / "src"))


def pytest_configure(config):
    """
    Hook de configuración de pytest para registrar marcadores personalizados.
    """
    config.addinivalue_line(
        "markers",
        "slow: marca las pruebas como lentas (deseleccionar con '-m \"not slow\"')",
    )
    config.addinivalue_line(
        "markers", "integration: marca las pruebas como pruebas de integración"
    )
    config.addinivalue_line("markers", "unit: marca las pruebas como pruebas unitarias")


# Fixtures globales que pueden ser usadas en cualquier test


@pytest.fixture
def precio_base_standar():
    """Precio base estándar para pruebas."""
    return 100.0


@pytest.fixture
def material_standar():
    """Material estándar para pruebas."""
    return "Madera"


@pytest.fixture
def color_standar():
    """Color estándar para pruebas."""
    return "Natural"

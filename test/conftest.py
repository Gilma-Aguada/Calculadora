import pytest
import calculadora
# --- FIXTURES ---
@pytest.fixture
def numeros_enteros():
    """Fixture con valores enteros para las pruebas."""
    return 10, 5

@pytest.fixture
def numeros_flotantes():
    """Fixture con valores flotantes para las pruebas."""
    return 0.1, 0.2
import pytest
from calculadora import sumar, restar, multiplicar, dividir



# --- 1. CASOS DE PRUEBA POR OPERACIÓN  ---

# Pruebas para SUMAR
@pytest.mark.smoke
def test_sumar_exito(numeros_enteros):
    a, b = numeros_enteros
    assert sumar(a, b) == 15

def test_sumar_flotantes(numeros_flotantes):
    a, b = numeros_flotantes
    # Usamos approx para comparar decimales en Python de forma segura
    assert sumar(a, b) == pytest.approx(0.3)

# Pruebas para RESTAR
def test_restar_exito(numeros_enteros):
    a, b = numeros_enteros
    assert restar(a, b) == 5

def test_restar_error():
    # Ejemplo de control de tipo o error esperado si aplica
    with pytest.raises(TypeError):
        restar(10, "5")

# Pruebas para MULTIPLICAR
def test_multiplicar_exito(numeros_enteros):
    a, b = numeros_enteros
    assert multiplicar(a, b) == 50

def test_multiplicar_flotantes(numeros_flotantes):
    a, b = numeros_flotantes
    assert multiplicar(a, b) == pytest.approx(0.02)

# Pruebas para DIVIDIR
@pytest.mark.exception
def test_dividir_exito(numeros_enteros):
    a, b = numeros_enteros
    assert dividir(a, b) == 2.0

def test_dividir_error_por_cero():
    # Verifica que lanzar ValueError al dividir por 0 funcione correctamente (Punto 1 - Error)
    with pytest.raises(ValueError):
        dividir(10, 0)
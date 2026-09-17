def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("Error: No se puede dividir por cero.")
    return a / b


"""
numero1 = float(input("Ingrese el primer número: "))
operador = input("Ingrese el operador (+): ")
numero2 = float(input("Ingrese el segundo número: "))

if operador == "+":
    resultado = numero1 + numero2
print("Resultado:", resultado)

numero1 = float(input("Ingrese el primer número: "))
operador = input("Ingrese el operador (-): ")
numero2 = float(input("Ingrese el segundo número: "))

if operador == "-":
    resultado = numero1 - numero2
print("Resultado:", resultado)
numero1 = float(input("Ingrese el primer número: "))
operador = input("Ingrese el operador (/): ")
numero2 = float(input("Ingrese el segundo número: "))

if operador == "/":
    resultado = numero1 / numero2
print("Resultado:", resultado)

numero1 = float(input("Ingrese el primer número: "))
operador = input("Ingrese el operador (*): ")
numero2 = float(input("Ingrese el segundo número: "))

if operador == "*":
    resultado = numero1 * numero2
print("Resultado:", resultado)
"""
"""
try:
    numero = int(input("Ingresa un número entero: "))
    resultado = 588/ numero
    print(f"588 / {numero} = {resultado}")
except ZeroDivisionError:
    print("Error: División por cero.")
except ValueError:
    print("Error: Entrada inválida, no es un número entero.")
finally:
    print("Operación finalizada.")
"""
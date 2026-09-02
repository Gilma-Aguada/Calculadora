"""
numero1 = float(input("Ingrese el primer número: "))
operador = input("Ingrese la operación (+, -, *, /): ")
numero2 = float(input("Ingrese el segundo número: "))

if operador == "+":
    resultado = numero1 + numero2
elif operador == "-":
    resultado = numero1 - numero2
elif operador == "*":
    resultado = numero1 * numero2
elif operador == "/":
    resultado = numero1 / numero2
else:
    resultado = "Operación no válida"

print("Resultado:", resultado)
"""
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

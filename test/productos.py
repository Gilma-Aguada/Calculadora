productos = []
def agregar_producto():
 
    try:
         nombre = input("nombre del producto: \n ").strip()
         if not nombre:
            print("El nombre del producto no puede estar vacío.")
            return
         precio = float(input("precio del producto: \n ").strip())

    except ValueError:
            print("Error: Debes ingresar valores válidos para el precio y la cantidad.")

            producto = {"nombre": nombre, "precio": precio}

            productos.append(producto)

            print(f"Producto : '{producto}' se agrego correctamente.")
    finally:
                print("Operación finalizada.")
 


   
def buscar_por_precio():
    print("Hola, soy buscar por precio")
def buscar_producto():
    print("Hola, soy buscar producto")
def eliminar_producto():
    print("Hola, soy eliminar producto")
def mostrar_estadisticas():
    print("Hola, soy mostrar estadisticas")
def mostrar_productos():
    print("Hola, soy mostrar productos")
    
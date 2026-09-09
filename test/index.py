from productos import agregar_producto, buscar_por_precio
from menu import mostrar_menu



from productos import(
    agregar_producto,
    buscar_por_precio,
    buscar_producto,
    eliminar_producto,
    mostrar_estadisticas,
    mostrar_productos,

)



def index():
    while True:
        mostrar_menu()
        op = input("Seleccionar: ").strip()
        match op:  
            case "1":
                agregar_producto()


if __name__ == "__main__":
    index()
            

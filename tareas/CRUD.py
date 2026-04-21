inventario = {
    "arroz": {"precio": 50, "stock": 5},
    "leche": {"precio": 60, "stock": 4},
    "aceite": {"precio": 150, "stock": 3},
    "azucar": {"precio": 45, "stock": 6},
    "habichuelas": {"precio": 80, "stock": 5}
}

def mostrar_menu():
    print("\n--- MENU PRINCIPAL ---")
    print("1. Ver productos disponibles")
    print("2. Comprar productos")
    print("3. Salir")

def mostrar_productos():
    print("\nListado de productos:")
    for nombre, datos in inventario.items():
        print(f"{nombre} - Precio: RD${datos['precio']} - Stock: {datos['stock']}")

# Bucle principal
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ").strip()

    # Opción 1: Ver productos
    if opcion == "1":
        mostrar_productos()

    # Opción 2: Comprar productos
    elif opcion == "2":
        total_compra = 0

        while True:
            mostrar_productos()
            producto = input(
                "\nIngrese el nombre del producto que desea comprar (o 'menu' para volver): "
            ).lower().strip()

            if producto == "menu":
                break

            if producto not in inventario:
                print("El producto ingresado no existe.")
                continue

            cantidad = input("Ingrese la cantidad deseada: ").strip()

            if not cantidad.isdigit():
                print("Debe ingresar un número válido.")
                continue

            cantidad = int(cantidad)

            if cantidad <= 0:
                print("La cantidad debe ser mayor que cero.")
                continue

            if cantidad > inventario[producto]["stock"]:
                print("No hay suficiente stock disponible.")
                continue

            costo = cantidad * inventario[producto]["precio"]
            inventario[producto]["stock"] -= cantidad
            total_compra += costo

            print(f"Compra registrada. Costo: RD${costo}")

            continuar = input("¿Desea agregar otro producto? (si/no): ").lower().strip()
            if continuar != "si":
                break

        print(f"\nTotal de la compra: RD${total_compra}")

    # Opción 3: Salir
    elif opcion == "3":
        print("\nPrograma finalizado.")
        break

    else:
        print("Opción inválida. Intente nuevamente.")

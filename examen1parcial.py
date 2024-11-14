# Datos de ejemplo del almacén
productos_almacen = {
    "Estantería A": [{"nombre": "Chocolate Amargo", "cantidad": 20, "precio": 2.5},
                     {"nombre": "Mermelada de Fresa", "cantidad": 15, "precio": 3.0}],
    "Estantería B": [{"nombre": "Aceitunas Verdes", "cantidad": 50, "precio": 1.5},
                     {"nombre": "Aceite de Oliva Extra", "cantidad": 10, "precio": 6.0}],
    "Estantería C": [{"nombre": "Café Molido", "cantidad": 25, "precio": 5.0},
                     {"nombre": "Té Verde", "cantidad": 40, "precio": 2.0}],
    "Estantería D": [{"nombre": "Pasta Integral", "cantidad": 30, "precio": 1.8},
                     {"nombre": "Arroz Basmati", "cantidad": 20, "precio": 1.7}]
}

# Diccionario para mapear letras a nombres completos de estanterías
mapa_estanterias = {
    "A": "Estantería A",
    "B": "Estantería B",
    "C": "Estantería C",
    "D": "Estantería D"
}

# Función para obtener el nombre completo de la estantería
def obtener_estanteria(letra):
    return mapa_estanterias.get(letra.upper(), letra)  # retorna la letra si no se encuentra en el mapa

# Función para agregar un producto al almacén
def agregar_producto():
    estanteria = obtener_estanteria(input("Introduce la estantería donde quieres agregar el producto (A, B, C, D): "))
    nombre = input("Introduce el nombre del producto: ")
    cantidad = int(input("Introduce la cantidad del producto: "))
    precio = float(input("Introduce el precio del producto: "))

    if estanteria not in productos_almacen:
        print(f"Error: La {estanteria} no existe.")
        return

    for producto in productos_almacen[estanteria]:
        if producto["nombre"] == nombre:
            print(f"Producto existente: {nombre} con {producto['cantidad']} unidades a {producto['precio']} euros cada una.")
            producto["cantidad"] += cantidad
            print(f"Producto {nombre} actualizado en {estanteria} con nueva cantidad {producto['cantidad']}.")
            return

    productos_almacen[estanteria].append({"nombre": nombre, "cantidad": cantidad, "precio": precio})
    print(f"Producto {nombre} agregado a {estanteria} con {cantidad} unidades a {precio} euros cada una.")

# Función para retirar productos del almacén
def retirar_producto():
    estanteria = obtener_estanteria(input("Introduce la estantería de la que quieres retirar el producto (A, B, C, D): "))
    nombre = input("Introduce el nombre del producto: ")
    cantidad = int(input("Introduce la cantidad a retirar: "))

    if estanteria not in productos_almacen:
        print(f"Error: La {estanteria} no existe.")
        return

    for producto in productos_almacen[estanteria]:
        if producto["nombre"] == nombre:
            print(f"Producto encontrado: {nombre} con {producto['cantidad']} unidades a {producto['precio']} euros cada una.")
            if producto["cantidad"] >= cantidad:
                producto["cantidad"] -= cantidad
                print(f"{cantidad} unidades de {nombre} retiradas de {estanteria}. Cantidad restante: {producto['cantidad']}")
                return
            else:
                print(f"Error: No hay suficiente cantidad de {nombre} en {estanteria}. Solo hay {producto['cantidad']} unidades.")
                return

    print(f"Error: El producto {nombre} no se encontró en {estanteria}.")

# Función para transferir productos entre estanterías
def transferir_producto():
    nombre = input("Introduce el nombre del producto a transferir: ")
    cantidad = int(input("Introduce la cantidad a transferir: "))
    origen = obtener_estanteria(input("Introduce la estantería de origen (A, B, C, D): "))
    destino = obtener_estanteria(input("Introduce la estantería de destino (A, B, C, D): "))

    if origen not in productos_almacen or destino not in productos_almacen:
        print(f"Error: Una de las estanterías {origen} o {destino} no existe.")
        return

    for producto in productos_almacen[origen]:
        if producto["nombre"] == nombre:
            if producto["cantidad"] >= cantidad:
                print(f"Producto encontrado en {origen}: {nombre} con {producto['cantidad']} unidades.")
                producto["cantidad"] -= cantidad
                for producto_destino in productos_almacen[destino]:
                    if producto_destino["nombre"] == nombre:
                        producto_destino["cantidad"] += cantidad
                        print(f"{cantidad} unidades de {nombre} transferidas de {origen} a {destino}.")
                        return
                productos_almacen[destino].append({"nombre": nombre, "cantidad": cantidad, "precio": producto["precio"]})
                print(f"{cantidad} unidades de {nombre} transferidas de {origen} a {destino}.")
                return
            else:
                print(f"Error: No hay suficiente cantidad de {nombre} en {origen}.")
                return

    print(f"Error: El producto {nombre} no se encontró en {origen}.")

# Función para verificar el estado del almacén
def estado_almacen():
    print("Estado actual del almacén:")
    for estanteria, productos in productos_almacen.items():
        print(f"{estanteria}:")
        for producto in productos:
            print(f" - {producto['nombre']}: {producto['cantidad']} unidades a {producto['precio']} euros cada una")
    print("\n")

# Función para optimización del inventario
def optimizar_inventario():
    max_valor, min_productos = None, None
    max_estanteria, min_estanteria = None, None

    for estanteria, productos in productos_almacen.items():
        valor_total = sum(p["cantidad"] * p["precio"] for p in productos)
        total_productos = sum(p["cantidad"] for p in productos)

        if max_valor is None or valor_total > max_valor:
            max_valor, max_estanteria = valor_total, estanteria
        if min_productos is None or total_productos < min_productos:
            min_productos, min_estanteria = total_productos, estanteria

    print(f"Estantería con mayor valor acumulado: {max_estanteria} con valor total de {max_valor} euros.")
    print(f"Estantería con menos productos: {min_estanteria} con {min_productos} unidades en total.")

# Función para verificar la disponibilidad de un producto en el almacén
def verificar_disponibilidad(nombre):
    encontrado = False
    for estanteria, productos in productos_almacen.items():
        for producto in productos:
            if producto["nombre"].lower() == nombre.lower():
                print(f"Producto encontrado: {nombre} en {estanteria} con {producto['cantidad']} unidades a {producto['precio']} euros cada una.")
                encontrado = True
    if not encontrado:
        print(f"El producto {nombre} no se encuentra en el almacén.")

# Menú principal
def menu():
    while True:
        print("\nMenú de Opciones:")
        print("1. Verificar el estado del almacén")
        print("2. Agregar productos")
        print("3. Retirar productos")
        print("4. Verificar disponibilidad de un producto")
        print("5. Transferir productos entre estanterías")
        print("6. Optimización del inventario")
        print("0. Salir")
        
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            estado_almacen()
        elif opcion == "2":
            agregar_producto()
        elif opcion == "3":
            retirar_producto()
        elif opcion == "4":
            nombre = input("Introduce el nombre del producto a verificar: ")
            verificar_disponibilidad(nombre)
        elif opcion == "5":
            transferir_producto()
        elif opcion == "6":
            optimizar_inventario()
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

# Ejecutar menú
menu()

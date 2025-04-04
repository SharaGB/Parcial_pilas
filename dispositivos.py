from collections import deque

def mostrar_menu():
    print("\nOpciones:")
    print("1. Registrar dispositivo")
    print("2. Prestar un dispositivo")
    print("3. Devolver un dispositivo")
    print("4. Modificar una venta")
    print("5. Mostrar inventario")
    print("6. Salir")


def registrar_dispositivo(inventario):
    while True:
        print("\nSeleccione el tipo de dispositivo a registrar:")
        print("1. PC")
        print("2. Tablet")
        opcion = input("Seleccione una opción: ")

        if opcion not in ["1", "2"]:
            print("Opción no válida. Intente de nuevo.")
            continue

        dispositivo = {}
        if opcion == "1":
            dispositivo["tipo"] = "PC"
        else:
            dispositivo["tipo"] = "Tablet"

        dispositivo["serial"] = input("Ingrese el serial del dispositivo: ")
        for item in inventario:
            if item["serial"] == dispositivo["serial"]:
                print("El serial ya existe en el inventario.")
                return

        dispositivo["marca"] = input("Ingrese la marca del dispositivo: ")

        if dispositivo["tipo"] == "PC":
            while True:
                try:
                    dispositivo["memoria_ram"] = int(input("Ingrese la memoria RAM: "))
                    if dispositivo["memoria_ram"] < 0:
                        print("La memoria RAM no puede ser negativa. Intente de nuevo.")
                        continue
                    break
                except ValueError:
                    print("Error: Asegúrese de ingresar un número válido.")

            while True:
                try:
                    dispositivo["disco_duro"] = int(input("Ingrese el tamaño del disco duro: "))
                    if dispositivo["disco_duro"] < 0:
                        print("El tamaño del disco duro no puede ser negativo. Intente de nuevo.")
                        continue
                    break
                except ValueError:
                    print("Error: Asegúrese de ingresar un número válido.")
        else:
            while True:
                try:
                    dispositivo["tamano"] = float(input("Ingrese el tamaño de la tablet (en pulgadas): "))
                    if dispositivo["tamano"] < 0:
                        print("El tamaño de la tablet no puede ser negativo. Intente de nuevo.")
                        continue
                    break
                except ValueError:
                    print("Error: Asegúrese de ingresar un número válido.")

        while True:
            try:
                dispositivo["precio"] = float(input("Ingrese el precio del dispositivo: "))
                if dispositivo["precio"] < 0:
                    print("El precio no puede ser negativo. Intente de nuevo.")
                    continue
                break
            except ValueError:
                print("Error: Asegúrese de ingresar un número válido.")

        dispositivo["nombre_usuario"] = ""
        dispositivo["disponible"] = True

        inventario.append(dispositivo)
        print("**** Dispositivo registrado exitosamente. ****")
        break


def prestar_dispositivo(inventario, prestamos):
    serial = input("Ingrese el serial del dispositivo a prestar: ")

    for dispositivo in inventario:
        if dispositivo["serial"] == serial:
            if not dispositivo["disponible"]:
                print("El dispositivo no está disponible.")
                return

            nombre_usuario = input("Ingrese el nombre del usuario que va a prestar el dispositivo: ")
            dispositivo["nombre_usuario"] = nombre_usuario
            dispositivo["disponible"] = False
            prestamos.append(dispositivo)
            print("**** Dispositivo prestado exitosamente. ****")
            print(f"El dispositivo se prestó a {nombre_usuario} con el N° de serial {serial}")
            return

    print("El serial no existe en el inventario.")


def devolver_dispositivo(inventario, prestamos):
    if not prestamos:
        print("No hay dispositivos en préstamo.")
        return

    dispositivo_serial = input("Ingrese el serial del dispositivo a devolver: ")

    dispositivo_a_devolver = None
    for dispositivo in prestamos:
        if dispositivo["serial"] == dispositivo_serial:
            dispositivo_a_devolver = dispositivo
            break

    if not dispositivo_a_devolver:
        print("El serial no existe en los préstamos.")
        return

    prestamos.remove(dispositivo_a_devolver)

    for item in inventario:
        if item["serial"] == dispositivo_a_devolver["serial"]:
            item["nombre_usuario"] = ""
            item["disponible"] = True
            print(f"**** Dispositivo con serial {item['serial']} devuelto exitosamente. ****")
            return


def modificar_dispositivo(inventario):
    serial = input("Ingrese el serial del dispositivo a modificar: ")

    dispositivo_a_modificar = None
    for dispositivo in inventario:
        if dispositivo["serial"] == serial:
            dispositivo_a_modificar = dispositivo
            break

    if not dispositivo_a_modificar:
        print("El serial no existe en el inventario.")
        return

    print("Datos actuales del dispositivo:")
    for key, value in dispositivo_a_modificar.items():
        print(f"{key}: {value}")

    print("\nIngrese los nuevos valores del dispositivo. ")
    nueva_marca = input("Nueva marca: ")
    if nueva_marca:
        dispositivo_a_modificar["marca"] = nueva_marca

    if dispositivo_a_modificar["tipo"] == "PC":
        while True:
            nueva_memoria_ram = input("Nueva memoria RAM: ")
            if nueva_memoria_ram:
                try:
                    nueva_memoria_ram = int(nueva_memoria_ram)
                    if nueva_memoria_ram < 0:
                        print("La memoria RAM no puede ser negativa. Intente de nuevo.")
                        continue
                    dispositivo_a_modificar["memoria_ram"] = nueva_memoria_ram
                    break
                except ValueError:
                    print("Error: Asegúrese de ingresar un número válido.")
            else:
                break

        while True:
            nuevo_disco_duro = input("Nuevo tamaño del disco duro: ")
            if nuevo_disco_duro:
                try:
                    nuevo_disco_duro = int(nuevo_disco_duro)
                    if nuevo_disco_duro < 0:
                        print("El tamaño del disco duro no puede ser negativo. Intente de nuevo.")
                        continue
                    dispositivo_a_modificar["disco_duro"] = nuevo_disco_duro
                    break
                except ValueError:
                    print("Error: Asegúrese de ingresar un número válido.")
            else:
                break
    else:
        while True:
            nuevo_tamano = input("Nuevo tamaño de la tablet (en pulgadas): ")
            if nuevo_tamano:
                try:
                    nuevo_tamano = float(nuevo_tamano)
                    if nuevo_tamano < 0:
                        print("El tamaño de la tablet no puede ser negativo. Intente de nuevo.")
                        continue
                    dispositivo_a_modificar["tamano"] = nuevo_tamano
                    break
                except ValueError:
                    print("Error: Asegúrese de ingresar un número válido.")
            else:
                break

    while True:
        nuevo_precio = input("Nuevo precio: ")
        if nuevo_precio:
            try:
                nuevo_precio = float(nuevo_precio)
                if nuevo_precio < 0:
                    print("El precio no puede ser negativo. Intente de nuevo.")
                    continue
                dispositivo_a_modificar["precio"] = nuevo_precio
                break
            except ValueError:
                print("Error: Asegúrese de ingresar un número válido.")
        else:
            break

    nuevo_nombre_usuario = input("Nuevo nombre del usuario: ")
    if nuevo_nombre_usuario:
        dispositivo_a_modificar["nombre_usuario"] = nuevo_nombre_usuario

    while True:
        nuevo_disponible = input("¿Está disponible el dispositivo? (True/False): ").strip().lower()
        if nuevo_disponible == "true":
            dispositivo_a_modificar["disponible"] = True
            break
        elif nuevo_disponible == "false":
            dispositivo_a_modificar["disponible"] = False
            break
        elif not nuevo_disponible:
            break
        else:
            print("Error: Debe ingresar 'True' o 'False'.")

    print("**** Dispositivo modificado exitosamente. ****")


def mostrar_inventario(inventario):
    if not inventario:
        print("El inventario está vacío.")
        return

    print("\nInventario:")
    for dispositivo in inventario:
        print(f"Serial: {dispositivo['serial']}")
        for key, value in dispositivo.items():
            if key != "serial":
                print(f"{key}: {value}")
        print("-" * 20)


def main():
    inventario = []  # Pila para almacenar los dispositivos
    prestamos = deque()  # Cola para gestionar los préstamos

    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            registrar_dispositivo(inventario)
        elif opcion == "2":
            prestar_dispositivo(inventario, prestamos)
        elif opcion == "3":
            devolver_dispositivo(inventario, prestamos)
        elif opcion == "4":
            modificar_dispositivo(inventario)
        elif opcion == "5":
            mostrar_inventario(inventario)
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()

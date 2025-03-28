def mostrar_menu():
    print("Opciones:")
    print("1. Registrar dispositivo")
    print("2. Prestar un dispositivo")
    print("3. Devolver un dispositivo")
    print("4. Modificar una venta")
    print("5. Mostrar inventario")
    print("6. Salir")


def registrar_dispositivo(inventario):
    print("\nSeleccione el tipo de dispositivo a registrar:")
    print("1. PC")
    print("2. Tablet")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        serial = input("Ingrese el serial del dispositivo: ")
        if serial in inventario:
            print("El serial ya existe en el inventario.")
            return

        marca = input("ingrese la marca del dispositivo: ")
        while True:
            try:
                memoria_ram = int(input("Ingrese la memoria_ram: "))
                if memoria_ram < 0:
                    print("Error: La memoria_ram no puede ser negativa.")
                    continue
                break
            except ValueError:
                print("Error: Asegúrese de ingresar un número válido.")

        while True:
            try:
                disco_duro = int(input("Ingrese el disco duro: "))
                if disco_duro < 0:
                    print("Error: El disco duro no puede ser negativo.")
                    continue
                break
            except ValueError:
                print("Error: Asegúrese de ingresar un número válido.")

        while True:
            try:
                precio = float(input("Ingrese el precio del producto: "))
                if precio < 0:
                    print("Error: El precio no puede ser negativo.")
                    continue
                break
            except ValueError:
                print("Error: Asegúrese de ingresar un número válido.")

        nombre_usuario = input("Ingrese el nombre del usuario: ")
        while True:
            try:
                disponible = bool(input("Ingrese si el dispositivo esta disponible (True/False): "))
                if disponible != True and disponible != False:
                    print("Error: El valor ingresado no es valido.")
                    continue
                break
            except ValueError:
                print("Error: Asegúrese de ingresar un valor booleano.")


        inventario[serial] = {"marca": marca, "memoria_ram": memoria_ram, "disco_duro": disco_duro, "precio": precio, "nombre_usuario": nombre_usuario, "disponible": disponible}
        print("Producto registrado exitosamente.")

    elif opcion == "2":
        serial = input("Ingrese el serial del dispositivo: ")
        if serial in inventario:
            print("El serial ya existe en el inventario.")
            return

        marca = input("ingrese la marca del dispositivo: ")
        while True:
            try:
                tamano = float(input("Ingrese el tamaño del dispositivo: "))
                if tamano < 0:
                    print("Error: El tamaño no puede ser negativo.")
                    continue
                break
            except ValueError:
                print("Error: Asegúrese de ingresar un número válido.")

        while True:
            try:
                precio = float(input("Ingrese el precio del dispositivo: "))
                if precio < 0:
                    print("Error: El precio no puede ser negativo.")
                    continue
                break
            except ValueError:
                print("Error: Asegúrese de ingresar un número válido.")

        nombre_usuario = input("Ingrese el nombre del usuario: ")
        while True:
            try:
                disponible = bool(input("Ingrese si el dispositivo esta disponible (True/False): "))
                if disponible != True and disponible != False:
                    print("Error: El valor ingresado no es valido.")
                    continue
                break
            except ValueError:
                print("Error: Asegúrese de ingresar un valor booleano.")

        inventario[serial] = {"marca": marca, "tamano": tamano, "precio": precio, "nombre_usuario": nombre_usuario, "disponible": disponible}
        print("Producto registrado exitosamente.")


def prestar_dispositivo(inventario):
    serial = input("Ingrese el serial del dispositivo a prestar: ")
    if serial not in inventario:
        print("El serial no existe en el inventario.")
        return
    
    if inventario[serial]["disponible"] == False:
        print("El dispositivo no esta disponible.")
        return
    
    nombre_usuario = input("Ingrese el nombre del usuario que va a prestar el dispositivo: ")
    inventario[serial]["nombre_usuario"] = nombre_usuario
    inventario[serial]["disponible"] = False
    print("Dispositivo prestado exitosamente.")
    print(f"El dispositivo se prestó a {nombre_usuario} con el serial {serial}")


def devolver_dispositivo(inventario):
    serial = input("Ingrese el serial del dispositivo a devolver: ")
    if serial not in inventario:
        print("El serial no existe en el inventario.")
        return
    
    if inventario[serial]["disponible"] == True:
        print("El dispositivo ya esta disponible.")
        return
    
    inventario[serial]["nombre_usuario"] = ""
    inventario[serial]["disponible"] = True
    print("Dispositivo devuelto exitosamente.")
    print(f"El dispositivo con serial {serial} está disponible: {inventario[serial]['disponible']}")


def modificar_dispositivo_pc(inventario):
    serial = input("Ingrese el serial del dispositivo a modificar: ")
    if serial not in inventario:
        print("El serial no existe en el inventario.")
        return
    print("Datos actuales:", inventario[serial])

    marca = input("Ingrese la nueva marca del dispositivo: ")
    while True:
        try:
            memoria_ram = int(input("Ingrese la nueva memoria_ram: "))
            if memoria_ram < 0:
                print("Error: La memoria_ram no puede ser negativa.")
                continue
            break
        except ValueError:
            print("Error: Asegúrese de ingresar un número válido.")

    while True:
        try:
            disco_duro = int(input("Ingrese el nuevo disco duro: "))
            if disco_duro < 0:
                print("Error: El disco duro no puede ser negativo.")
                continue
            break
        except ValueError:
            print("Error: Asegúrese de ingresar un número válido.")

    while True:
        try:
            precio = float(input("Ingrese el nuevo precio del producto: "))
            if precio < 0:
                print("Error: El precio no puede ser negativo.")
                continue
            break
        except ValueError:
            print("Error: Asegúrese de ingresar un número válido.")

    nombre_usuario = input("Ingrese el nuevo nombre del usuario: ")
    
    while True:
        try:
            disponible = bool(input("Ingrese si el dispositivo esta disponible (True/False): "))
            if disponible != True and disponible != False:
                print("Error: El valor ingresado no es valido.")
                continue
            break
        except ValueError:
            print("Error: Asegúrese de ingresar un valor booleano.")

    if marca:
        inventario[serial]["marca"] = marca
    if memoria_ram:
        inventario[serial]["memoria_ram"] = memoria_ram
    if disco_duro:
        inventario[serial]["disco_duro"] = disco_duro
    if precio:
        inventario[serial]["precio"] = precio
    if nombre_usuario:
        inventario[serial]["nombre_usuario"] = nombre_usuario
    if disponible:
        inventario[serial]["disponible"] = disponible
    
    print("Dispositivo modificado exitosamente.")


def mostrar_inventario(inventario):
    if not inventario:
        print("El inventario está vacío.")
        return
    print("Inventario:")

    if inventario:
        for serial, dispositivo in inventario.items():
            print(f"Serial: {serial}")
            for key, value in dispositivo.items():
                print(f"{key}: {value}")


def main():
    inventario = {}

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_dispositivo(inventario)
        elif opcion == "2":
            prestar_dispositivo(inventario)
        elif opcion == "3":
            devolver_dispositivo(inventario)
        elif opcion == "4":
            modificar_dispositivo_pc(inventario)
        elif opcion == "5":
            mostrar_inventario(inventario)
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()

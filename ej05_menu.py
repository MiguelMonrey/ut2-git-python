opcion = int(input("1. Saludar\n2. Despedirse\n3. Salir\nElige una opción: "))

match opcion:
    case 1:
        print("¡Hola!")
    case 2:
        print("¡Adiós!")
    case 3:
        print("Hasta pronto")
    case _:
        print("Opción no válida")

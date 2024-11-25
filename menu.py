from operaciones import sumar, restar, multiplicar, dividir

def mostrar_menu():
    print("1- Sumar")
    print("2- Restar")
    print("3- Multiplicar")
    print("4- Dividir")
    print("5- Salir")
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        a, b = map(float, input("Introduce dos números separados por espacio: ").split())
        print("Resultado:", sumar(a, b))
    elif opcion == "2":
        a, b = map(float, input("Introduce dos números separados por espacio: ").split())
        print("Resultado:", restar(a, b))
    elif opcion == "3":
        a, b = map(float, input("Introduce dos números separados por espacio: ").split())
        print("Resultado:", multiplicar(a, b))
    elif opcion == "4":
        try:
            a, b = map(float, input("Introduce dos números separados por espacio: ").split())
            print("Resultado:", dividir(a, b))
        except ZeroDivisionError:
            print("Error: No se puede dividir entre 0.")
        except ValueError as e:
            print("Error:", e)
    elif opcion == "5":
        print("Saliendo del programa...")
    else:
        print("Opción no válida.")
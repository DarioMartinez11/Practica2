<<<<<<< HEAD

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
        a, b = map(float, input("Introduce dos números separados por espacio: ").split())
        print("Resultado:", dividir(a, b))
    elif opcion == "5":
        print("Saliendo del programa...")
    else:
        print("Opción no válida.")

        elif opcion == "6":
        try:
            n = int(input("Introduce un número: "))
            print("Resultado:", factorial_recursivo(n))
        except ValueError as e:
            print("Error:", e)

      
=======
from operaciones import sumar, restar, multiplicar, dividir, factorial_iterativo

def mostrar_menu():
    while True:
        print("\nMenú de opciones:")
        print("1- Sumar")
        print("2- Restar")
        print("3- Multiplicar")
        print("4- Dividir")
        print("5- Salir")
        print("6- Calcular el factorial de un número (iterativo)")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            try:
                a, b = map(float, input("Introduce dos números separados por espacio: ").split())
                print("Resultado:", sumar(a, b))
            except ValueError:
                print("Error: Debes ingresar números válidos.")
        elif opcion == "2":
            try:
                a, b = map(float, input("Introduce dos números separados por espacio: ").split())
                print("Resultado:", restar(a, b))
            except ValueError:
                print("Error: Debes ingresar números válidos.")
        elif opcion == "3":
            try:
                a, b = map(float, input("Introduce dos números separados por espacio: ").split())
                print("Resultado:", multiplicar(a, b))
            except ValueError:
                print("Error: Debes ingresar números válidos.")
        elif opcion == "4":
            try:
                a, b = map(float, input("Introduce dos números separados por espacio: ").split())
                print("Resultado:", dividir(a, b))
            except ZeroDivisionError:
                print("Error: No se puede dividir entre 0.")
            except ValueError:
                print("Error: Debes ingresar números válidos.")
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        elif opcion == "6":
            try:
                n = int(input("Introduce un número entero no negativo: "))
                print("Resultado:", factorial_iterativo(n))
            except ValueError:
                print("Error: Debes ingresar un número entero no negativo.")
        else:
            print("Opción no válida. Inténtalo de nuevo.")
>>>>>>> 38bd2abd22c686deb0cf8efa8c38511fe87c5058

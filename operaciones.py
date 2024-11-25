# operaciones.py

def sumar(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b
    else:
        raise ValueError("Ambos parámetros deben ser int o float.")

def restar(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a - b
    else:
        raise ValueError("Ambos parámetros deben ser int o float.")

def multiplicar(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        b = int(b)  # Convertimos b a entero para evitar el error de range con floats
        resultado = 0
        for _ in range(abs(b)):  # Multiplicamos usando sumas
            resultado += abs(a)

        if (a < 0 and b > 0) or (a > 0 and b < 0):
            resultado = -resultado  # Ajustamos el signo
        return resultado
    else:
        raise ValueError("Ambos parámetros deben ser int o float.")

def dividir(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Ambos parámetros deben ser int o float.")
    if b == 0:
        raise ZeroDivisionError("El divisor no puede ser cero.")
    
    cociente = 0
    acumulador = abs(a)
    divisor = abs(b)
    while acumulador >= divisor:
        acumulador -= divisor
        cociente += 1
    
    if (a < 0) ^ (b < 0):  # XOR para verificar si los signos son opuestos
        cociente = -cociente
    return cociente

def factorial_iterativo(n):
    """
    Calcula el factorial de un número de forma iterativa.
    :param n: Número entero no negativo.
    :return: Factorial de n.
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("El número debe ser un entero no negativo.")
    
    resultado = 1
    for i in range(1, n + 1):  # Empieza en 1 y va hasta n (inclusive)
        resultado *= i
    
    return resultado

def factorial_recursivo(n):
    """
    Calcula el factorial de un número de forma recursiva.
    :param n: Número entero no negativo.
    :return: Factorial de n.
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("El número debe ser un entero no negativo.")
    
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursivo(n - 1)

def fibonacci(n):
    """
    Calcula el número de Fibonacci de manera iterativa.
    :param n: Número entero no negativo.
    :return: El número de Fibonacci en la posición n.
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("El número debe ser un entero no negativo.")
    
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


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
        resultado = 0
        for _ in range(abs(b)):
            resultado += abs(a)
        if (a < 0 and b > 0) or (a > 0 and b < 0):
            resultado = -resultado
        return resultado
    else:
        raise ValueError("Ambos parámetros deben ser int o float.")

def factorial_recursivo(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("El número debe ser un entero no negativo.")
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursivo(n - 1)


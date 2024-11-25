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
    if (a < 0) ^ (b < 0):  # XOR para verificar signos opuestos
        cociente = -cociente
    return cociente
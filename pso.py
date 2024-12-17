import math

def rastrigin(x: list) -> float:
    """
    Calcula o valor da função de Rastrigin para um vetor x.
    
    :param x: Lista de valores (vetor x)
    :return: Resultado da função de Rastrigin
    """
    d = len(x)  # Dimensão do vetor
    resultado = 10 * d  # Termo constante 10d
    for xi in x:
        resultado += xi**2 - 10 * math.cos(2 * math.pi * xi)
    return resultado

# Exemplo de uso
x = [0, 0]  # Ponto no espaço de busca
resultado = rastrigin(x)
print(f"O valor da função de Rastrigin no ponto {x} é: {resultado}")

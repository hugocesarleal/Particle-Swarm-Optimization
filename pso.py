import math

def calcular_equacao(equacao: str, x1: float, x2: float) -> float:
    """
    Avalia uma equação dada em termos de x1 e x2 e retorna o resultado.

    :param equacao: A equação como string, por exemplo "sqrt(x1**2) + x2"
    :param x1: Valor de x1
    :param x2: Valor de x2
    :return: O resultado da equação
    """
    try:
        # Permite o uso de funções matemáticas como sqrt
        contexto = {"x1": x1, "x2": x2, "sqrt": math.sqrt, "__builtins__": None}
        resultado = eval(equacao, contexto)
        return resultado
    except Exception as e:
        raise ValueError(f"Erro ao calcular a equação: {e}")

# Exemplo de uso
equacao = "sqrt(x1**2) + x2**2"
x1 = -3
x2 = 4
resultado = calcular_equacao(equacao, x1, x2)
print(f"O resultado da equação '{equacao}' para x1={x1} e x2={x2} é: {resultado}")

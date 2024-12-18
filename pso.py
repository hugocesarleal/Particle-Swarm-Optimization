import math
import random
import numpy as np
import matplotlib.pyplot as plt
from visualizacao import atualizar_grafico, inicializar_grafico

def fit(x):
    d = len(x)
    resultado = 10 * d 
    for xi in x:
        resultado += xi**2 - 10 * math.cos(2 * math.pi * xi)
    return resultado

def calcular_fitness(lista_de_itens):
    lista_fitness = [fit(item) for item in lista_de_itens]
    return lista_fitness

def solInicial(n, d, limInf, limSup):
    if limInf > limSup:
        raise ValueError("O valor mínimo do intervalo deve ser menor ou igual ao valor máximo.")
    
    vetor = [
        tuple(random.uniform(limInf, limSup) for _ in range(d))
        for _ in range(n)
    ]
    return vetor

def calcularVelocidades(w, c1, c2, particulas, velocidades, pBest, gBest, nDimensoes):
    novasVelocidades = []
    cognitivo = [tuple(x1 - x2 for x1, x2 in zip(tupla1, tupla2)) for tupla1, tupla2 in zip(pBest, particulas)]
    social = [tuple(x - y for x, y in zip(gBest, tupla)) for tupla in particulas]
    
    i = 0
    for v in velocidades:
        velocidade = tuple((
        (w * v[d]) + (c1 * cognitivo[i][d]) + (c2 * social[i][d]) 
        for d in range(nDimensoes)))
        novasVelocidades.append(velocidade)
        i += 1
    return novasVelocidades

def pso(maxIter, w, c1, c2, qtdeParticulas, nDimensoes, limInf, limSup, plotar):
    particulas = solInicial(qtdeParticulas, nDimensoes, limInf, limSup)
    velocidades = solInicial(qtdeParticulas, nDimensoes, limInf, limSup)
    fitness = calcular_fitness(particulas)
    pBest = particulas
    gBest = particulas[fitness.index(min(fitness))]
    ftMedia = []
    ftgBest = []

    if plotar:
        fig, ax = inicializar_grafico()
    
    for iter in range(maxIter):
        velocidades = calcularVelocidades(w, c1, c2, particulas, velocidades, pBest, gBest, nDimensoes)
        
        for i in range(qtdeParticulas):
            p = particulas[i]
            v = velocidades[i]

            novaPosicao = tuple(a + b for a, b in zip(p, v))
            particulas[i] = novaPosicao

            if fit(novaPosicao) < fit(pBest[i]):
                pBest[i] = novaPosicao

            if fit(novaPosicao) < fit(gBest):
                gBest = novaPosicao

        if plotar:
            atualizar_grafico(ax, particulas, iter, intervalo=0.1)

        ftMedia.append(sum(fitness) / len(fitness))
        ftgBest.append(fit(gBest))

    if plotar:
        plt.show()

    return gBest

def arredondar_solucao(tupla, casas_decimais=4):
    return tuple(round(coordenada, casas_decimais) for coordenada in tupla)

if __name__ == "__main__":
    maxIter = 50
    w = 0.5
    c1 = 1.3
    c2 = 1.5
    qtdeParticulas = 5000
    nDimensoes = 2
    limInf = -5.12
    limSup = 5.12
    plotar = True

    sol = pso(maxIter, w, c1, c2, qtdeParticulas, nDimensoes, limInf, limSup, plotar)

    sol_arredondada = arredondar_solucao(sol)

    print(sol_arredondada)
    print("Fitness: ",round(fit(sol),4))
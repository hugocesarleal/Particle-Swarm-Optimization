import math
import random
import numpy as np
import matplotlib.pyplot as plt
from visualizacao import atualizarGrafico, inicializarGrafico

def fit(x):
    x = np.array(x)  # Convert tuple to numpy array
    n = len(x)

    # Critérios de penalização
    r = 10
    s = 12

    # Cálculo do fitness
    fx = 10 * n + np.sum(x**2 - 10 * np.cos(2 * np.pi * x))  # Fitness do indivíduo
    gx = np.sum(r * np.maximum(0, np.sin(2 * np.pi * x) + 0.5))   # gi(x) desigualdade
    hx = np.sum(s * np.abs(np.cos(2 * np.pi * x) + 0.5))        # hi(x0) igualdade
    resultado = fx + gx + hx                                # Fitness com penalizações aplicadas

    return resultado

def calcularFitness(listaDeItens):
    listaFitness = [fit(item) for item in listaDeItens]
    return listaFitness

def gX(coordenada):
    g = math.sin(2*math.pi*coordenada) + 0.5
    return g < 0

def hX(coordenada):
    h = math.cos(2*math.pi*coordenada) + 0.5
    return h == 0

def solInicial(n, d, limInf, limSup):
    if limInf > limSup:
        raise ValueError("O valor mínimo do intervalo deve ser menor ou igual ao valor máximo.")
    
    vetor = [
        tuple(random.uniform(limInf, limSup) for _ in range(d))
        for _ in range(n)
    ]
    return vetor

def calcularVelocidades(w, c1, c2, particulas, velocidades, pBest, gBest, nDimensoes, vMax):
    novasVelocidades = []
    cognitivo = [tuple(x1 - x2 for x1, x2 in zip(tupla1, tupla2)) for tupla1, tupla2 in zip(pBest, particulas)]
    social = [tuple(x - y for x, y in zip(gBest, tupla)) for tupla in particulas]
    
    i = 0
    for v in velocidades:
        velocidade = tuple((w * v[d]) + (c1 * random.random() * cognitivo[i][d]) + (c2 * random.random() * social[i][d]) for d in range(nDimensoes))
        # Limitar a velocidade
        velocidade = tuple(max(min(vel, vMax), -vMax) for vel in velocidade)
        novasVelocidades.append(velocidade)
        i += 1
    return novasVelocidades

def pso(maxIter, w, c1, c2, qtdeParticulas, nDimensoes, limInf, limSup, plotar):
    particulas = solInicial(qtdeParticulas, nDimensoes, limInf, limSup)
    velocidades = solInicial(qtdeParticulas, nDimensoes, limInf, limSup)
    fitness = calcularFitness(particulas)
    pBest = particulas
    gBest = particulas[fitness.index(min(fitness))]
    ftMedia = []
    ftDesvioPadrao = []
    ftGBest = []
    vMax = (limSup - limInf) * 0.1  # Limite de velocidade

    if plotar:
        fig, ax = inicializarGrafico()
    
    for iter in range(maxIter):
        # Inércia adaptativa
        w = 0.9 - (0.5 * iter / maxIter)
        
        velocidades = calcularVelocidades(w, c1, c2, particulas, velocidades, pBest, gBest, nDimensoes, vMax)
        
        for i in range(qtdeParticulas):
            p = particulas[i]
            v = velocidades[i]

            novaPosicao = tuple(a + b for a, b in zip(p, v))
            particulas[i] = novaPosicao

            if fit(novaPosicao) < fit(pBest[i]):
                pBest[i] = novaPosicao

            if fit(novaPosicao) < fit(gBest):
                gBest = novaPosicao

        fitness = calcularFitness(particulas)
        ftMedia.append(sum(fitness) / len(fitness))
        ftDesvioPadrao.append(np.std(fitness))
        ftGBest.append(fit(gBest))

        if plotar:
            atualizarGrafico(ax, particulas, iter, gBest, intervalo=0.1)

    if plotar:
        plt.show()

    mediaFitnessTotal = sum(ftMedia) / len(ftMedia)
    return gBest, ftMedia, ftDesvioPadrao, mediaFitnessTotal

if __name__ == "__main__":
    maxIter = 100
    w = 0.5
    c1 = 1.3
    c2 = 0.05
    qtdeParticulas = 500
    nDimensoes = 2
    limInf = -5.12
    limSup = 5.12
    plotar = True

    sol, ftMedia, ftDesvioPadrao, mediaFitnessTotal = pso(maxIter, w, c1, c2, qtdeParticulas, nDimensoes, limInf, limSup, plotar)

    print("Melhor solução: ", sol)
    print("Melhor Fitness: ", fit(sol))
    print("Média da Fitness Total: ", mediaFitnessTotal)

    # Plotar a média da fitness por geração
    plt.figure()
    plt.plot(range(maxIter), ftMedia, label='Média da Fitness')
    plt.xlabel('Geração')
    plt.ylabel('Média da Fitness')
    plt.title('Média da Fitness por Geração')
    plt.legend()
    plt.show()

    # Plotar o desvio padrão da fitness por geração
    plt.figure()
    plt.plot(range(maxIter), ftDesvioPadrao, label='Desvio Padrão da Fitness', color='red')
    plt.xlabel('Geração')
    plt.ylabel('Desvio Padrão da Fitness')
    plt.title('Desvio Padrão da Fitness por Geração')
    plt.legend()
    plt.show()
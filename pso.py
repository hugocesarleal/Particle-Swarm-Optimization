from visualizacao import atualizarGrafico, inicializarGrafico, plotarEstatisticas
import matplotlib.pyplot as plt
import numpy as np
import random
import time

def fit(x):
    #Função de fitness que calcula o valor de aptidão de uma partícula
    x = np.array(x)
    n = len(x)
    r = 10
    s = 12

    fx = 10 * n + np.sum(x**2 - 10 * np.cos(2 * np.pi * x)) #Função de Rastrigin
    gx = np.sum(r * np.maximum(0, np.sin(2 * np.pi * x) + 0.5)) #Penalidade gx
    hx = np.sum(s * np.abs(np.cos(2 * np.pi * x) + 0.5)) #Penalidade hx

    penalizacao = 1000 * np.sum((x + 1/3)**2) #Penalidade adicional
    resultado = fx + gx + hx + penalizacao #Soma de todas as penalidades e a função de Rastrigin
    return resultado

def fx(x):
    #Função de Rastrigin
    x = np.array(x)
    n = len(x)
    
    return 10 * n + np.sum(x**2 - 10 * np.cos(2 * np.pi * x))

def calcularFitness(listaDeItens):
    #Calcula o fitness de uma lista de partículas
    listaFitness = [fit(item) for item in listaDeItens]
    return listaFitness

def solInicial(n, d, limInf, limSup):
    #Gera uma solução inicial aleatória dentro dos limites especificados
    if limInf > limSup:
        raise ValueError("O valor mínimo do intervalo deve ser menor ou igual ao valor máximo.")
    vetor = [
        tuple(random.uniform(limInf, limSup) for _ in range(d))
        for _ in range(n)
    ]
    return vetor

def calcularVelocidades(w, c1, c2, particulas, velocidades, pBest, gBest, nDimensoes, vMax):
    #Calcula as novas velocidades das partículas
    novasVelocidades = []
    cognitivo = [tuple(x1 - x2 for x1, x2 in zip(tupla1, tupla2)) for tupla1, tupla2 in zip(pBest, particulas)] #Componente cognitivo
    social = [tuple(x - y for x, y in zip(gBest, tupla)) for tupla in particulas] #Componente social

    i = 0
    for v in velocidades:
        velocidade = tuple((w * v[d]) + (c1 * random.random() * cognitivo[i][d]) + (c2 * random.random() * social[i][d]) for d in range(nDimensoes)) #Nova velocidade
        velocidade = tuple(max(min(vel, vMax), -vMax) for vel in velocidade) #Limita a velocidade máxima
        novasVelocidades.append(velocidade)
        i += 1

    return novasVelocidades

def pso(maxIter, w, c1, c2, qtdeParticulas, nDimensoes, limInf, limSup, plotar):
    #Função principal do algoritmo PSO
    particulas = solInicial(qtdeParticulas, nDimensoes, limInf, limSup) #Inicializa partículas
    velocidades = solInicial(qtdeParticulas, nDimensoes, limInf, limSup) #Inicializa velocidades
    fitness = calcularFitness(particulas) #Calcula o fitness inicial
    pBest = particulas #Melhor posição individual
    gBest = particulas[fitness.index(min(fitness))] #Melhor posição global
    vMax = (limSup - limInf) * 0.1 #Velocidade máxima
    mediasFitness = [] #Lista para armazenar a média do fitness
    desviosFitness = [] #Lista para armazenar o desvio padrão do fitness
    iteracoes = [] #Lista para armazenar as iterações

    if plotar:
        fig, ax = inicializarGrafico() #Inicializa o gráfico

    for iter in range(maxIter):
        wAdaptativa = 0.9 - (w * iter / maxIter) #Calcula o peso adaptativo
        velocidades = calcularVelocidades(wAdaptativa, c1, c2, particulas, velocidades, pBest, gBest, nDimensoes, vMax) #Atualiza as velocidades
        
        for i in range(qtdeParticulas):
            p = particulas[i]
            v = velocidades[i]

            novaPosicao = tuple(a + b for a, b in zip(p, v)) #Calcula a nova posição
            particulas[i] = novaPosicao
            
            if fit(novaPosicao) < fit(pBest[i]):
                pBest[i] = novaPosicao #Atualiza a melhor posição individual
            
            if fit(novaPosicao) < fit(gBest):
                gBest = novaPosicao #Atualiza a melhor posição global
        
        fitness = calcularFitness(particulas) #Recalcula o fitness
        mediasFitness.append(np.mean(fitness)) #Armazena a média do fitness
        desviosFitness.append(np.std(fitness)) #Armazena o desvio padrão do fitness
        iteracoes.append(iter) #Armazena a iteração atual
        
        if plotar:
            atualizarGrafico(ax, particulas, iter, gBest, intervalo=0.1) #Atualiza o gráfico
    
    if plotar:
        plt.show() #Mostra o gráfico
    
        plotarEstatisticas(iteracoes, mediasFitness, desviosFitness) #Plota as estatísticas
    
    return gBest #Retorna a melhor posição global

if __name__ == "__main__":
    #Parâmetros do algoritmo PSO
    maxIter = 100
    w = 0.5
    c1 = 1.3
    c2 = 0.5
    qtdeParticulas = 500
    nDimensoes = 5
    limInf = -5.12
    limSup = 5.12
    plotar = False

    tempoInicio = time.time() #Marca o tempo de início
    sol = pso(maxIter, w, c1, c2, qtdeParticulas, nDimensoes, limInf, limSup, plotar) #Executa o PSO
    tempoFim = time.time() #Marca o tempo de fim

    print("Melhor solução: ", sol) #Imprime a melhor solução
    print("Melhor Fitness: ", fx(sol)) #Imprime o melhor fitness
    print("Tempo de execução: ", tempoFim - tempoInicio, "segundos") #Imprime o tempo de execução
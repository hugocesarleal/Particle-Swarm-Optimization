import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plotarParticulas(particulas, ax):
    from pso import fx
    xVals = [p[0] for p in particulas]
    yVals = [p[1] for p in particulas]
    zVals = [fx(p) for p in particulas]
    ax.scatter(xVals, yVals, zVals, c=zVals, cmap='viridis')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Fitness')

def inicializarGrafico():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.set_zlim(0, 200)
    return fig, ax

def atualizarGrafico(ax, particulas, iteracao, gBest, intervalo=0.1):
    from pso import fit
    xLim = ax.get_xlim()
    yLim = ax.get_ylim()
    zLim = ax.get_zlim()
    ax.cla()
    plotarParticulas(particulas, ax)
    fitness_gBest = fit(gBest)
    gBest_formatado = tuple(f"{coord:.5f}" for coord in gBest)
    ax.set_title(f'Iteração: {iteracao+1} | gBest: {gBest_formatado} | Fitness: {fitness_gBest:.5f}')
    ax.set_xlim(xLim)
    ax.set_ylim(yLim)
    ax.set_zlim(zLim)
    plt.pause(intervalo)

def plotarEstatisticas(iteracoes, medias, desvios):
    plt.figure()
    plt.plot(iteracoes, medias, label='Média do Fitness')
    plt.plot(iteracoes, desvios, label='Desvio Padrão do Fitness')
    plt.xlabel('Iterações')
    plt.ylabel('Valores')
    plt.title('Média e Desvio Padrão do Fitness ao longo das Iterações')
    plt.legend()
    plt.show()
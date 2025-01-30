import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plotarParticulas(particulas, ax):
    from pso import fit
    xVals = [p[0] for p in particulas]
    yVals = [p[1] for p in particulas]
    zVals = [fit(p) for p in particulas]
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

def atualizarGrafico(ax, particulas, iteracao, intervalo=0.1):
    xLim = ax.get_xlim()
    yLim = ax.get_ylim()
    zLim = ax.get_zlim()
    ax.cla()
    plotarParticulas(particulas, ax)
    ax.set_title(f'Iteração: {iteracao+1}')
    ax.set_xlim(xLim)
    ax.set_ylim(yLim)
    ax.set_zlim(zLim)
    plt.pause(intervalo)
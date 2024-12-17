import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plotar_particulas(particulas, ax):
    """
    Plota as partículas em um gráfico 3D.
    :param particulas: Lista de partículas, onde cada partícula é uma tupla (x, y).
    :param ax: O eixo do gráfico 3D onde as partículas serão plotadas.
    """
    from pso import fit  # Importação local da função fit
    
    x_vals = [p[0] for p in particulas]
    y_vals = [p[1] for p in particulas]
    z_vals = [fit(p) for p in particulas]  # Calcula o fitness para cada partícula

    ax.scatter(x_vals, y_vals, z_vals, c=z_vals, cmap='viridis')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Fitness')

def inicializar_grafico():
    """
    Inicializa e retorna o gráfico 3D.
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    return fig, ax

def atualizar_grafico(ax, particulas, intervalo=0.1):
    """
    Atualiza o gráfico 3D com as novas posições das partículas.
    :param ax: O eixo do gráfico 3D.
    :param particulas: Lista de partículas, onde cada partícula é uma tupla (x, y).
    :param intervalo: Intervalo de tempo (em segundos) entre as atualizações do gráfico.
    """
    ax.cla()  # Limpa o gráfico anterior
    plotar_particulas(particulas, ax)
    plt.pause(intervalo)

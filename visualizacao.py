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
    Inicializa e retorna o gráfico 3D com limites fixos.
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Definindo os limites fixos para os eixos
    ax.set_xlim(-5, 5)  # Limites de X
    ax.set_ylim(-5, 5)  # Limites de Y
    ax.set_zlim(0, 200)  # Limites de Z (fitness)
    
    return fig, ax

def atualizar_grafico(ax, particulas, iteracao, intervalo=0.1):
    """
    Atualiza o gráfico 3D com as novas posições das partículas, mantendo os limites fixos,
    e exibe a iteração atual no título do gráfico.
    :param ax: O eixo do gráfico 3D.
    :param particulas: Lista de partículas, onde cada partícula é uma tupla (x, y).
    :param iteracao: Número da iteração atual.
    :param intervalo: Intervalo de tempo (em segundos) entre as atualizações do gráfico.
    """
    # Salvar os limites fixos antes de limpar o gráfico
    x_lim = ax.get_xlim()
    y_lim = ax.get_ylim()
    z_lim = ax.get_zlim()

    ax.cla()  # Limpa o gráfico anterior
    plotar_particulas(particulas, ax)
    
    # Atualiza o título com o número da iteração
    ax.set_title(f'Iteração: {iteracao+1}')
    
    # Restaurar os limites após a atualização
    ax.set_xlim(x_lim)
    ax.set_ylim(y_lim)
    ax.set_zlim(z_lim)
    
    plt.pause(intervalo)

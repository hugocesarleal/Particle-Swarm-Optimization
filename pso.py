import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time

def gerar_coordenadas(n_pontos):
    return [(round(random.uniform(0, 5), 1), 
             round(random.uniform(0, 5), 1), 
             round(random.uniform(0, 5), 1)) for _ in range(n_pontos)]

def atualizar_grafico(n_pontos, n_atualizacoes, delay=0.5):
    # Configurar figura e eixo 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for _ in range(n_atualizacoes):
        # Gerar novos pontos
        coordenadas = gerar_coordenadas(n_pontos)
        x = [p[0] for p in coordenadas]
        y = [p[1] for p in coordenadas]
        z = [p[2] for p in coordenadas]

        # Limpar o gráfico antigo e plotar os novos pontos
        ax.cla()  # Clear axis
        ax.scatter(x, y, z, c='blue', marker='o')

        # Personalizar os eixos
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        # Atualizar a figura
        plt.draw()
        plt.pause(delay)  # Espera entre atualizações

    plt.show()

# Configurações
n_pontos = 1000        # Número de pontos
n_atualizacoes = 100  # Número de atualizações
atualizar_grafico(n_pontos, n_atualizacoes, delay=0.1)

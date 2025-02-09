# Otimização por Enxame de Partículas (PSO)

Este projeto é um trabalho da disciplina de Inteligência Artificial que implementa o algoritmo de Otimização por Enxame de Partículas (PSO). O objetivo é encontrar a melhor solução para uma função de fitness, utilizando partículas que se movem pelo espaço de busca.

## Arquivos

- `pso.py`: Implementa o algoritmo PSO e a função de fitness.
- `visualizacao.py`: Contém funções para visualização das partículas e das estatísticas de fitness.

## Como Executar

1. Certifique-se de ter o Python e as bibliotecas necessárias instaladas:
    ```sh
    pip install matplotlib numpy
    ```

2. Execute o script [pso.py](http://_vscodecontentref_/0):
    ```sh
    python pso.py
    ```

## Parâmetros do Algoritmo

Os parâmetros do algoritmo PSO podem ser ajustados diretamente no arquivo [pso.py](http://_vscodecontentref_/1):
- [maxIter](http://_vscodecontentref_/2): Número máximo de iterações.
- [w](http://_vscodecontentref_/3): Peso inercial.
- [c1](http://_vscodecontentref_/4): Coeficiente cognitivo.
- [c2](http://_vscodecontentref_/5): Coeficiente social.
- [qtdeParticulas](http://_vscodecontentref_/6): Quantidade de partículas.
- [nDimensoes](http://_vscodecontentref_/7): Número de dimensões do espaço de busca.
- [limInf](http://_vscodecontentref_/8): Limite inferior do espaço de busca.
- [limSup](http://_vscodecontentref_/9): Limite superior do espaço de busca.
- [plotar](http://_vscodecontentref_/10): Booleano para ativar/desativar a visualização.

## Visualização

O projeto inclui visualizações em 3D das partículas e gráficos das estatísticas de fitness ao longo das iterações. Para ativar a visualização, defina [plotar = True](http://_vscodecontentref_/11) no arquivo [pso.py](http://_vscodecontentref_/12).
# Otimização por Enxame de Partículas (PSO)

Este projeto é um trabalho da disciplina de Inteligência Artificial que implementa o algoritmo de Otimização por Enxame de Partículas (PSO). O objetivo é encontrar a melhor solução para uma função de fitness, utilizando partículas que se movem pelo espaço de busca.

# Publicado em:
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.15019195.svg)](https://doi.org/10.5281/zenodo.15019195)

## Arquivos

- `pso.py`: Implementa o algoritmo PSO e a função de fitness.
- `visualizacao.py`: Contém funções para visualização das partículas e das estatísticas de fitness.
- `Relatório PSO.pdf`: Relatório detalhado do projeto.

## Como Executar

1. Certifique-se de ter o Python e as bibliotecas necessárias instaladas:
    ```sh
    pip install matplotlib numpy
    ```

2. Execute o script **pso.py**:
    ```sh
    python pso.py
    ```

## Parâmetros do Algoritmo

Os parâmetros do algoritmo PSO podem ser ajustados diretamente no arquivo **pso.py**:
- `maxIter`: Número máximo de iterações.
- `w`: Peso inercial.
- `c1`: Coeficiente cognitivo.
- `c2`: Coeficiente social.
- `qtdeParticulas`: Quantidade de partículas.
- `nDimensoes`: Número de dimensões do espaço de busca.
- `limInf`: Limite inferior do espaço de busca.
- `limSup`: Limite superior do espaço de busca.
- `plotar`: Booleano para ativar/desativar a visualização.

## Visualização

O projeto inclui visualizações em 3D das partículas e gráficos das estatísticas de fitness ao longo das iterações. Para ativar a visualização, defina `plotar = True` no arquivo **pso.py**.

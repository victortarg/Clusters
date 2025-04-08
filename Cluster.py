# instalar as bibliotecas:
# pip install networkx
#pip install matplotlib

# import numpy as np
# import networkx as nx
# import matplotlib.pyplot as plt

# Parte 1: Funções auxiliares para percorrer grafos (DFS) e para transpor o grafo (inverter direções das arestas)
def dfs(grafo, v, visitado, componente):
    visitado[v] = True
    componente.append(v)
    for i in range(len(grafo)):
        if grafo[v][i] and not visitado[i]:
            dfs(grafo, i, visitado, componente)

def transpor_grafo(matriz):
    n = len(matriz)
    transposta = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            transposta[j][i] = matriz[i][j]
    return transposta

# Parte 2: Função que faz a primeira DFS no grafo original e empilha os nós por ordem de término
def preenche_ordem(grafo, v, visitado, pilha):
    visitado[v] = True
    for i in range(len(grafo)):
        if grafo[v][i] and not visitado[i]:
            preenche_ordem(grafo, i, visitado, pilha)
    pilha.append(v)

# Parte 3: Função principal que aplica o algoritmo de Kosaraju para encontrar os componentes fortemente conectados
def kosaraju_matriz(matriz):
    n = len(matriz)  #numero de vertices nno grafo
    visitado = [False] * n # lista de visitados, iniciando todos False
    pilha = [] # pilha que vai ser adicionado com os vertices em ordem de termino do DFS

    # aplicar DFS em todos os vertices e preenche a pilha.
    for i in range(n):
        if not visitado[i]:     
            preenche_ordem(matriz, i, visitado, pilha)

    transposta = transpor_grafo(matriz) #transpor o grafo
    visitado = [False] * n #limpa a lista de visitados antes de começar o segundo DFS
    componentes = [] #Lista que vai armazenar os componentes fortemente conectados (achar os clusters)

    #enquanto nao ta vazio.
    while pilha:
        v = pilha.pop() #retira os vertices da pilha
        if not visitado[v]: # se o vertice nao foi visitado, realiza o dfs no grafo transposto
            componente = [] #Lista que vai armazenar os componentes fortemente conectados (achar os clusters)
            dfs(transposta, v, visitado, componente) #aplica do DFS
            componentes.append(componente) # adiciona a componente encontrada a lista de componentes

    return componentes # retornar a lista com os componentes fortemente ligados.

# Parte 4: Utiliza os componentes fortemente conectados para sugerir novas amizades (arestas ausentes dentro do SCC)
def sugerir_amizades_matriz(matriz):
    componentes = kosaraju_matriz(matriz)
    print("Componentes fortemente conectados:")
    for comp in componentes:
        print(comp)

    print("\nSugestões de amizade:")
    for comp in componentes:
        for u in comp:
            for v in comp:
                if u != v and matriz[u][v] == 0:
                    print(f"Sugestão: usuário {u} → seguir usuário {v}")

matriz = [
    [0, 1, 1, 0, 0, 0],  # 0
    [0, 0, 1, 0, 0, 0],  # 1
    [1, 0, 0, 0, 0, 0],  # 2
    [0, 0, 0, 0, 1, 0],  # 3
    [0, 0, 0, 0, 0, 1],  # 4
    [1, 0, 0, 1, 0, 0],  # 5
]

sugerir_amizades_matriz(matriz)

#caso precise de um teste mais robusto.
# matriz = [
#     [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 0
#     [1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 1
#     [1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 2
#     [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 3
#     [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 4
#     [0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 5
#     [0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 6
#     [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 7
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # 8
#     [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # 9
#     [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # 10
#     [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 11
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # 12
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],  # 13
#     [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],  # 14
#     [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],  # 15
#     [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],  # 16
#     [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],  # 17
#     [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1],  # 18
#     [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],  # 19
# ]

#parte aonde é feita a representação da matriz para grafo.
# matriz_desenho = np.array(matriz)
# grafo = nx.from_numpy_array(matriz_desenho)

# nx.draw(grafo, with_labels=True, node_color='lightblue', node_size=500, font_size=10)
# plt.show()

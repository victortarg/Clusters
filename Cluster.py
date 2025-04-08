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

def preenche_ordem(grafo, v, visitado, pilha):
    visitado[v] = True
    for i in range(len(grafo)):
        if grafo[v][i] and not visitado[i]:
            preenche_ordem(grafo, i, visitado, pilha)
    pilha.append(v)

def kosaraju_matriz(matriz):
    n = len(matriz)
    visitado = [False] * n
    pilha = []

    for i in range(n):
        if not visitado[i]:
            preenche_ordem(matriz, i, visitado, pilha)

    transposta = transpor_grafo(matriz)
    visitado = [False] * n
    componentes = []

    while pilha:
        v = pilha.pop()
        if not visitado[v]:
            componente = []
            dfs(transposta, v, visitado, componente)
            componentes.append(componente)

    return componentes

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
    [0, 0, 0, 1, 0, 0],  # 5
]

sugerir_amizades_matriz(matriz)


# C:\Users\jpkab\OneDrive\Desktop\doc\Cenario2\Cluster.py
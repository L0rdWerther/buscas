# Busca em profundidade (DFS) verme
def dfs(grafo, inicio, fim, caminho=None, visitados=None):
    if caminho is None:
        caminho = [inicio]
    if visitados is None:
        visitados = set()

    visitados.add(inicio)

    if inicio == fim:
        return caminho

    for vizinho, _ in grafo[inicio]:
        if vizinho not in visitados:
            novo_caminho = dfs(grafo, vizinho, fim, caminho + [vizinho], visitados)
            if novo_caminho:
                return novo_caminho

    return None

# Busca em largura (BFS) fungo
def bfs(grafo, inicio, fim):
    fila = [(inicio, [inicio])]
    visitados = set()

    while fila:
        vertice, caminho = fila.pop(0)
        visitados.add(vertice)

        if vertice == fim:
            return caminho

        for (vizinho, distancia) in grafo[vertice]:
            if vizinho not in visitados:
                fila.append((vizinho, caminho + [vizinho]))
                visitados.add(vizinho)

    return None
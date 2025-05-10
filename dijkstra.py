# Caminho usando Dijkstra (menor custo)
def dijkstra(grafo, inicio, fim):
    distancias = {vertice: float('infinity') for vertice in grafo}
    distancias[inicio] = 0
    nao_visitados = list(grafo.keys())
    caminhos = {inicio: [inicio]}

    while nao_visitados:
        vertice_atual = min(nao_visitados, key=lambda vertice: distancias[vertice])
        nao_visitados.remove(vertice_atual)

        if vertice_atual == fim:
            return caminhos[vertice_atual]

        for vizinho, peso in grafo[vertice_atual]:
            nova_distancia = distancias[vertice_atual] + peso
            if nova_distancia < distancias[vizinho]:
                distancias[vizinho] = nova_distancia
                caminhos[vizinho] = caminhos[vertice_atual] + [vizinho]

    return None
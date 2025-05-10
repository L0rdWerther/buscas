# Busca gananciosa (greedy)
def busca_gananciosa(grafo, inicio, fim, heuristica):
    visitados = set()
    fila = [(inicio, [inicio])]

    while fila:
        # Ordena a fila com base na heurística
        fila.sort(key=lambda x: heuristica[x[0]])
        vertice_atual, caminho = fila.pop(0)

        if vertice_atual in visitados:
            continue

        visitados.add(vertice_atual)

        if vertice_atual == fim:
            return caminho

        for vizinho, _ in grafo[vertice_atual]:
            if vizinho not in visitados:
                fila.append((vizinho, caminho + [vizinho]))

    return None
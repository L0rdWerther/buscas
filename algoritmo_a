# Busca algoritmo a*
def algoritmo_a(grid, inicio, fim, heuristica, obstaculos):
    visitados = set()
    fila = [(inicio, [inicio], 0)]  # se faz necessário guardar o custo acumulado

    while fila:
        # Ordena a fila com base em f(n) = g(n) + h(n)
        fila.sort(key=lambda g: g[2] + heuristica[g[0]])
        vertice_atual, caminho, custo_atual = fila.pop(0)

        if vertice_atual in visitados:
            continue

        visitados.add(vertice_atual)

        if vertice_atual == fim:
            return caminho

        for vizinho, peso in grid[vertice_atual]:
            if vizinho in obstaculos:
                continue  # Ignora obstáculos
            if vizinho not in visitados:
                novo_custo = custo_atual + peso  # custo acumulado até o vizinho
                fila.append((vizinho, caminho + [vizinho], novo_custo))
                print(caminho + [vizinho], ",", novo_custo)

    return None

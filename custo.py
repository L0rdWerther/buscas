# Calcula o custo de um caminho
def calcular_custo(grafo, caminho):
    if not caminho or len(caminho) < 2:
        return 0  # Sem custo se o caminho for vazio ou tiver apenas um nó

    custo_total = 0
    for i in range(len(caminho) - 1):
        origem = caminho[i]
        destino = caminho[i + 1]
        for vizinho, peso in grafo[origem]:
            if vizinho == destino:
                custo_total += peso
                break
    return custo_total
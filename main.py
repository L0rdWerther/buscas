from grafo_1 import grafo, heuristica
from ganancia import busca_gananciosa
from custo import calcular_custo
from dfs_bfs import dfs, bfs
from dijkstra import dijkstra

# Executa as buscas e exibe os resultados
def executar_buscas(grafo, cidade_inicial, cidade_final):
    caminho_bfs = bfs(grafo, cidade_inicial, cidade_final)
    caminho_dfs = dfs(grafo, cidade_inicial, cidade_final)
    caminho_dijkstra = dijkstra(grafo, cidade_inicial, cidade_final)
    caminho_ganancioso = busca_gananciosa(grafo, cidade_inicial, cidade_final, heuristica)

    if caminho_bfs:
        custo_bfs = calcular_custo(grafo, caminho_bfs)
        print("Caminho BFS:", " -> ".join(caminho_bfs), "| Custo:", custo_bfs)
    else:
        print("Sem caminho BFS entre", cidade_inicial, "e", cidade_final)

    if caminho_dfs:
        custo_dfs = calcular_custo(grafo, caminho_dfs)
        print("Caminho DFS:", " -> ".join(caminho_dfs), "| Custo:", custo_dfs)
    else:
        print("Sem caminho DFS entre", cidade_inicial, "e", cidade_final)

    if caminho_dijkstra:
        custo_dijkstra = calcular_custo(grafo, caminho_dijkstra)
        print("Caminho Dijkstra:", " -> ".join(caminho_dijkstra), "| Custo:", custo_dijkstra)
    else:
        print("Sem caminho Dijkstra entre", cidade_inicial, "e", cidade_final)

    if caminho_ganancioso:
        custo_ganancioso = calcular_custo(grafo, caminho_ganancioso)
        print("Caminho ganancioso:", " -> ".join(caminho_ganancioso), "| Custo:", custo_ganancioso)
    else:
        print("Sem caminho ganancioso entre", cidade_inicial, "e", cidade_final)



def main():
    cidade_inicial = input("cidade inicial: ").upper()
    cidade_final = input("cidade final: ").upper()

    executar_buscas(grafo, cidade_inicial, cidade_final)

if __name__ == "__main__":
    main()
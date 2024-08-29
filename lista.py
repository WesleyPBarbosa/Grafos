class Grafo:
    def __init__(lista, num_vertices):
        lista.num_vertices = num_vertices
        lista.lista_adjacencia = [[] for _ in range(num_vertices)]

    def adicionar(lista, origem, destino):
        lista.lista_adjacencia[origem].append(destino)
        lista.lista_adjacencia[destino].append(origem)  # Para grafos não direcionados

    def remover(lista, origem, destino):
        lista.lista_adjacencia[origem].remove(destino)
        lista.lista_adjacencia[destino].remove(origem)  # Para grafos não direcionados

    def imprimir_lista(lista):
        for i in range(lista.num_vertices):
            print(f"{i}: ", end="")
            print(" ".join(map(str, lista.lista_adjacencia[i])))

# Exemplo de uso
if __name__ == "__main__":
    num_vertices = 5
    g = Grafo(num_vertices)

    g.adicionar_aresta(0, 1)
    g.adicionar_aresta(0, 4)
    g.adicionar_aresta(1, 2)
    g.adicionar_aresta(1, 3)
    g.adicionar_aresta(1, 4)
    g.adicionar_aresta(2, 3)
    g.adicionar_aresta(3, 4)

    print("Lista de Adjacência:")
    g.imprimir()

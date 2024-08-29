class Grafo:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.lista_adjacencia = [[] for _ in range(num_vertices)]

    def adicionar_aresta(self, origem, destino):
        self.lista_adjacencia[origem].append(destino)
        self.lista_adjacencia[destino].append(origem)  # Para grafos não direcionados

    def obter_arestas(self):
        arestas = []
        for u in range(self.num_vertices):
            for v in self.lista_adjacencia[u]:
                if u < v:  # Para evitar duplicações (grafos não orientados)
                    arestas.append((u, v))
        return arestas

def produto_cartesiano(grafo1, grafo2):
    num_vertices_grafo1 = grafo1.num_vertices
    num_vertices_grafo2 = grafo2.num_vertices
    num_vertices_resultante = num_vertices_grafo1 * num_vertices_grafo2

    grafo_resultante = Grafo(num_vertices_resultante)

    for u1 in range(num_vertices_grafo1):
        for u2 in range(num_vertices_grafo2):
            for v1 in grafo1.lista_adjacencia[u1]:
                vertice1 = u1 * num_vertices_grafo2 + u2
                vertice2 = v1 * num_vertices_grafo2 + u2
                grafo_resultante.adicionar_aresta(vertice1, vertice2)

            for v2 in grafo2.lista_adjacencia[u2]:
                vertice1 = u1 * num_vertices_grafo2 + u2
                vertice2 = u1 * num_vertices_grafo2 + v2
                grafo_resultante.adicionar_aresta(vertice1, vertice2)

    return grafo_resultante

def imprimir_grafo(grafo):
    for i in range(grafo.num_vertices):
        print(f"{i}: ", end="")
        print(" ".join(map(str, grafo.lista_adjacencia[i])))

# Exemplo de uso
if __name__ == "__main__":
    # Grafo 1
    g1 = Grafo(2)
    g1.adicionar_aresta(0, 1)

    # Grafo 2
    g2 = Grafo(3)
    g2.adicionar_aresta(0, 1)
    g2.adicionar_aresta(1, 2)

    # Produto Cartesiano
    grafo_produto = produto_cartesiano(g1, g2)

    print("Grafo resultante do Produto Cartesiano:")
    imprimir_grafo(grafo_produto)

from lista import Grafo

class op:
    def obter_arestas(vergrafo):
        arestas = []
        for u in range(vergrafo.num_vertices):
            for v in vergrafo.lista_adjacencia[u]:
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
            vertice1 = u1 * num_vertices_grafo2 + u2
            
            # Verifica arestas no grafo1, mantendo u2 fixo
            for v1 in grafo1.lista_adjacencia[u1]:
                vertice2 = v1 * num_vertices_grafo2 + u2
                if vertice2 not in grafo_resultante.lista_adjacencia[vertice1]:
                    grafo_resultante.adicionar(vertice1, vertice2)

            # Verifica arestas no grafo2, mantendo u1 fixo
            for v2 in grafo2.lista_adjacencia[u2]:
                vertice2 = u1 * num_vertices_grafo2 + v2
                if vertice2 not in grafo_resultante.lista_adjacencia[vertice1]:
                    grafo_resultante.adicionar(vertice1, vertice2)

    return grafo_resultante

def imprimir_grafo(grafo):
    for i in range(grafo.num_vertices):
        print(f"{i}: ", end="")
        print(" ".join(map(str, grafo.lista_adjacencia[i])))

# Exemplo de uso
if __name__ == "__main__":
    # Grafo 1
    g1 = Grafo(2)
    g1.adicionar(0, 1)

    # Grafo 2
    g2 = Grafo(3)
    g2.adicionar(0, 1)
    g2.adicionar(1, 2)

    # Produto Cartesiano
    grafo_produto = produto_cartesiano(g1, g2)

    print("Grafo resultante do Produto Cartesiano:")
    imprimir_grafo(grafo_produto)

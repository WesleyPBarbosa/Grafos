import numpy as np

def criaMatriz(v):
    matriz=[]
    for i in range (v):
        matriz.append([])
        for j in range (v):
            matriz[i].append(0)
    return matriz

def add(a,b, m):
    m[a][b] = 1
    m[b][a] = 1

def rm(a,b, m):
    m[a][b] = 0
    m[b][a] = 0

def imprimir_matriz(matriz):
    print("  ", end="")
    for i in range(len(matriz)):
        print(i, end=" ")
    print()

    for i, linha in enumerate(matriz):
        print(f"{i}: ", end="")
        print(" ".join(map(str, linha)))

print("Começo")
print("-----------------")
matriz = criaMatriz(4)
imprimir_matriz(matriz)
print("-----------------")
add(0, 1,matriz)
add(0, 3,matriz)
add(1, 2,matriz)
add(1, 3,matriz)
add(2, 3,matriz)
print("Após as altereções")
print("-----------------")
imprimir_matriz(matriz)
print("-----------------")
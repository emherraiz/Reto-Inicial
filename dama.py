import numpy as np
n = 4
tablero = np.zeros((n,n))
tablero_prueba = [[1, 0, 0, 0],[0, 0, 1, 0],[1, 0, 0, 0],[0, 0, 0, 1]]

def dama_atacada(tablero):
    atacada = False
    n = len(tablero)
    for fila in tablero:
        if sum(fila) > 1:
            atacada = True

    tablero_transpuesta = np.transpose(tablero)

    for columna in tablero_transpuesta:
        if sum(columna) > 1:
            atacada = True

    n_diagonales = 2*n-1
    suma = 0
    for i in range(n):
        if suma > 1:
            atacada = True
        suma = 0
        for k in range(n_diagonales):
            if tablero[i][i+k] == 1:
                suma += 1

    return atacada

for x in range(-2, 2):
    print(x)


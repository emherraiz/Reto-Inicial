import numpy as np
n = 3
tablero = np.zeros((n,n))
tablero_prueba = [[1, 0, 0, 0],[0, 0, 1, 0],[1, 0, 0, 0],[0, 0, 0, 1]]

def dama_atacada(tablero):
    for fila in tablero:
        if sum(fila) > 1:
            return True
        if

print(dama_atacada(tablero_prueba))


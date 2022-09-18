import numpy as np

n = 4
tablero = np.zeros((n,n))
tablero_prueba = [[1, 0, 0],[0, 0, 1],[0, 0, 0]]

def n_damas(tablero):
    suma = 0
    for fila in tablero:
        suma += sum(fila)

    if suma == len(tablero):
        return True
    else:
        return False

def rotar_tablero(tablero):
    return [[tablero[j][i] for j in range(len(tablero))] for i in range(len(tablero[0])-1,-1,-1)]


def dama_atacada(tablero):

    n = len(tablero)
    for fila in tablero:
        if sum(fila) > 1:
            return True

    tablero_transpuesta = np.transpose(tablero)

    for columna in tablero_transpuesta:
        if sum(columna) > 1:
            return True

    tablero_rotado = rotar_tablero(tablero)

    for diagonal in range(-n, n-1):
        suma_diagonal_principal = 0
        suma_diagonal_secundaria = 0
        for i in range(n-1, -1, -1):
            diagonal += 1
            if 0 <= diagonal < n:
                if tablero[i][diagonal] == 1:
                    suma_diagonal_principal += 1

                if tablero_rotado[i][diagonal] == 1:
                    suma_diagonal_secundaria += 1

        if suma_diagonal_principal > 1 or suma_diagonal_secundaria > 1:
            return True


    return False


print(dama_atacada(tablero_prueba))

#n=dim , (x,y)=colocacion primera dama
def posibilidad(n,x,y):
    tablero=np.zeros((n,n))
    tablero[x,y]=1
    for fila in range(n):
        for casilla in range(n):
            tablero[fila][casilla]=1
            if dama_atacada(tablero)==False:
                pass
            else:
                tablero[fila][casilla]=0
    return tablero

def tableros_posibles(n):
    tableros=[]
    for i in range(n):
        for j in range(n):
            #if posibilidad(n,i,j) not in tableros:
                tableros.append(posibilidad(n,i,j))
    return tableros

print(tableros_posibles(3))

#Falta eliminar tableros repetidos de la lista tableros y
#crear un bucle para que siga buscando tableros que no esten en esa lista hasta que
#len(tableros)=n*n
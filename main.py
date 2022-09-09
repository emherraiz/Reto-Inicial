tablero = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['a', 0, 'a']]
posibles_saltos = [[1, 2], [-1, 2], [1, -2], [-1, -2], [2, 1], [2, -1], [-2, 1], [-2, -1]]
suma = 0

def en_el_tablero(i, j):
    if 0 <= i <= 3 and 0 <= j <=2:
        return True
    else:
        return False


def posicion(i, j, numero_de_saltos, suma = 0, salto_actual = 0):
    for k in posibles_saltos:
        salto_i = i+k[0]
        salto_j = j+k[1]
        if en_el_tablero(salto_i, salto_j):
            if isinstance(tablero[salto_i][salto_j], int):
                suma += 1

    if salto_actual != numero_de_saltos:
        posicion(salto_i, salto_j, numero_de_saltos, suma, salto_actual + 1)


for i in range(4):
    for j in range(3):
        for k in posibles_saltos:
            if isinstance(tablero[i][j], int):
                salto_i = i+k[0]
                salto_j = j+k[1]
                if en_el_tablero(salto_i, salto_j):
                    if isinstance(tablero[salto_i][salto_j], int):
                        suma += 1

print(suma)


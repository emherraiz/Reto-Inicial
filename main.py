tablero = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['a', 0, 'a']]
posibles_saltos = [[1, 2], [-1, 2], [1, -2], [-1, -2], [2, 1], [2, -1], [-2, 1], [-2, -1]]


def en_el_tablero(i, j):
    if 0 <= i <= 3 and 0 <= j <=2:
        return True
    else:
        return False


def posibilidades_validas(i, j, numero_de_saltos_inicial, numero_de_saltos_actual, suma_final = 0):
    if numero_de_saltos_actual == 0:
        for k in posibles_saltos:
            salto_i = i+k[0]
            salto_j = j+k[1]
            if en_el_tablero(salto_i, salto_j) and isinstance(tablero[salto_i][salto_j], int):
                if numero_de_saltos_actual == 0:
                    suma += 1

    else:
        for k in posibles_saltos:
            salto_i = i+k[0]
            salto_j = j+k[1]
            if en_el_tablero(salto_i, salto_j) and isinstance(tablero[salto_i][salto_j], int):
                numero_de_saltos_actual -= 1
                suma += posibilidades_validas(i, j, numero_de_saltos_inicial, numero_de_saltos_actual, suma)
    
    return suma



'''
    for i in range(4):
        for j in range(3):
            if isinstance(tablero[i][j], int):
                for k in posibles_saltos:
                    salto_i = i+k[0]
                    salto_j = j+k[1]
                    if en_el_tablero(salto_i, salto_j):
                        if isinstance(tablero[salto_i][salto_j], int):
                            suma += 1

'''

suma_final = 0
for x in range(4):
    for y in range(3):
        if isinstance(tablero[x][y], int):
            suma_final += posibilidades_validas(x, y, 2)

print(suma_final)


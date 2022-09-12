tablero = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['a', 0, 'a']]
posibles_saltos = [[1, 2], [-1, 2], [1, -2], [-1, -2], [2, 1], [2, -1], [-2, 1], [-2, -1]]


def en_el_tablero(i, j):
    if 0 <= i <= 3 and 0 <= j <=2:
        return True
    else:
        return False


def posibilidades_validas_por_posicion(i, j, numero_de_saltos, suma = 0):
    numero_de_saltos -= 1
    for k in posibles_saltos:
        salto_i = i+k[0]
        salto_j = j+k[1]
        if en_el_tablero(salto_i, salto_j) and isinstance(tablero[salto_i][salto_j], int):
            if numero_de_saltos == 0:
                suma += 1

            else:
                suma = posibilidades_validas_por_posicion(salto_i, salto_j, numero_de_saltos, suma)

    return suma


def posibilidades_validas(numero_de_saltos):
    suma_final = 0
    for i in range(4):
        for j in range(3):
            if isinstance(tablero[i][j], int):
                suma_final += posibilidades_validas_por_posicion(i, j, numero_de_saltos)

    return suma_final


print(posibilidades_validas(3))


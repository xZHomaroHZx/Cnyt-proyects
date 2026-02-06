#matrices de prueba
# Matrices base
A = [[1, 0, 0, 1], [2, 2]]   # identidad 2x2
B = [[2, 1, 1, 2], [2, 2]]   # simétrica
C = [[0, -1, 1, 0], [2, 2]]  # antisimétrica
D = [[1, 2, 3, 4], [2, 2]]   # normal
E = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [3, 3]] # 3x3

#propiedades
assert cuadrada(A) == True
assert cuadrada(E) == True

assert simetrica(B) == True
assert simetrica(D) == False

assert antisimetrica(C) == True
assert antisimetrica(B) == False

assert ortogonal(A) == True   # identidad siempre es ortogonal

#Pruebas operaciones
assert cuadrada(A) == True
assert cuadrada(E) == True

assert simetrica(B) == True
assert simetrica(D) == False

assert antisimetrica(C) == True
assert antisimetrica(B) == False

assert ortogonal(A) == True   # identidad siempre es ortogonal

#Pruebas de producto
M1 = [[1,2,3,4], [2,2]]
M2 = [[5,6,7,8], [2,2]]

Prod = producto(M1, M2)
assert Prod[0] == [19,22,43,50]

#Potencia
I = Midentidad(2)

assert potencia(I, 5)[0] == [1,0,0,1]

assert potencia(A, 2)[0] == [1,0,0,1]  # identidad al cuadrado sigue siendo identidad

#Determinantes
M2x2 = [[1,2,3,4],[2,2]]
assert det(M2x2) == -2

M3 = [[1,0,0,0,1,0,0,0,1],[3,3]]
assert det(M3) == 1

#Traspuesta 
T = traspuesta(D)
assert T[0] == [1,3,2,4]

#submatriz
SM = submatriz(E,1,1)
assert SM[1] == [2,2]   # queda 2x2

#Inversa
M = [[1,2,3,4],[2,2]]
Inv = inversa(M)

# multiplicar por su inversa debe dar identidad
check = producto(M, Inv)
assert check[0][0] == 1

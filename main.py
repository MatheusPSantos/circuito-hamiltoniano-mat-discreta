#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#função que multiplica matrizes
def mult_matrix(bool_matrix, alpha_matrix):

    new_matrix = []

    for i in range(len(bool_matrix)):
        new_row = []
        for j in range(len(bool_matrix)):
            new_element = ''
            for mult in range(len(bool_matrix)):
                if(bool_matrix[i][mult]):
                    new_element = new_element + alpha_matrix[mult][j]
            new_row.append(new_element)
        new_matrix.append(new_row)

    return new_matrix

# Método Exato: Método "Composição Latina"
print("Método da \"Composição Latina\"")
# passando o tamanho das matriz a ser inserida
tam = input("Tamanho da matriz >>> ")
print(tam)

qi = tam
gj = tam
# matrizes a seram manipuladas
mtzA = []
mtzB = []
for i in range(qi):
    mtzA.append([])
    for j in range(gj):
        tmp = input("Valor >>> ")
        mtzA[i].append(tmp)
print("Matriz de adjacência A : ")
print(mtzA)

for i in range(qi):
    mtzB.append([])
    for j in range(gj):
        tmp = input("Letra >>> ")
        mtzB[i].append(tmp)
print("Matriz de adjacência B : ")
print(mtzB)

# matrizes auxiliares

mtzP2 = []
mtzP2 = mult_matrix(mtzA, mtzB)
print(mtzP2)
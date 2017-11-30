#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#função que multiplica matrizes
def multiplicar_matrizes(mat1, mat2, mat3, tam):
    for i in range(tam):
        for j in range(tam):
            acumula = '0'
            for k in range(tam):
                acumula = acumula + mat1[i][k]*mat2[k][j]
            mat3[i][j] = acumula
    return mat3

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
mtzP1 = []
mtzP1 = mtzA

mtzP2 = []
mtzP2 = multiplicar_matrizes(mtzB, mtzP1, mtzP2, tam)
print(mtzP2)
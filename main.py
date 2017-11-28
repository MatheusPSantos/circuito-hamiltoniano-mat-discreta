#!/usr/bin/env python3
# -*- coding: utf-8 -*-
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

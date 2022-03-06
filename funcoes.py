import random
from math import sqrt
import matplotlib.pyplot as plt


def gerar_matriz(tamanho):
    matriz = []
    for i in range(tamanho):
        par = []

        x = random.randrange(-100, 100)
        par.append(x)
        y = random.randrange(-100, 100)
        par.append(y)
        matriz.append(par)
    return matriz


def calcula_dist(matriz, ponto):
    dist = None
    X = 0
    Y = 0
    for c in range(len(matriz)):
        x = matriz[c][0] - ponto[0]
        y = matriz[c][1] - ponto[1]
        hipo = sqrt(x ** 2 + y ** 2)
        if dist is None:
            dist = hipo

        if hipo < dist:
            dist = hipo
            X = matriz[c][0]
            Y = matriz[c][1]
    menor_ponto = [X, Y]
    print(menor_ponto)
    return dist, menor_ponto


def gera_grafico(matriz, menor_ponto, ponto):
    x = []
    y = []

    for c in range(len(matriz)):
        x.append(matriz[c][0])
        y.append(matriz[c][1])

    A = [menor_ponto[0], ponto[0]]
    B = [menor_ponto[1], ponto[1]]
    # Pontos aleatorios
    plt.scatter(x, y, color='blue')
    # Ponto de menor distancia
    plt.scatter(menor_ponto[0], menor_ponto[1], color='red')
    # Ponto arbitrario
    plt.scatter(ponto[0], ponto[1], color='green')
    # Plot da linha
    plt.plot(A, B, color='black')
    plt.show()

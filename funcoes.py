import random
from math import sqrt
import matplotlib.pyplot as plt


def inputs():
    # Condição do loop while
    i = True
    # Definindo valor para x e y no intuito de evitar possiveis erros de ponteiros nulos
    x, y = 0, 0
    # Inputs do usuario
    tamanho = int(input('Informe o numero de pontos aleatorios a serem gerados: '))
    # Loop para garantir que o usuario vai botar valores dentro do range
    while i:
        x = int(input('Informe o valor x do ponto arbitrario(entre -100 e 100): '))
        y = int(input('Informe o valor y do ponto arbitrario(entre -100 e 100): '))

        if -100 <= x <= 100 and -100 <= x <= 100:
            i = False
        else:
            print('valores invalidos, informe novamente!')
    return tamanho, x, y


# Gera matriz de numeros aleatorios
def gerar_matriz(tamanho):
    # Instancia uma lista vazia
    matriz = []

    # Loop que gera numeros aleatorios, alem de popular uma matriz com estes numeros
    for i in range(tamanho):
        par = []

        # Adicionando os numeros em variaveis intermediarias
        x = random.randrange(-100, 100)
        par.append(x)
        y = random.randrange(-100, 100)
        par.append(y)

        # Adiciona os pares x, y a matriz
        matriz.append(par)
    return matriz


# Calcula o ponto mais proximo do ponto arbitrario e sua distancia
def calcula_dist(matriz, ponto):
    dist = None
    X = 0
    Y = 0
    # Testa cada ponto para saber o mais proximo
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

    # Cria uma variavel para armazenar o ponto mais proximo ao arbitrario
    menor_ponto = [X, Y]
    return dist, menor_ponto


# Gerador do grafico
def gera_grafico(matriz, menor_ponto, ponto):
    # Instancia duas lista vazia
    x = []
    y = []

    # Gera duas listas contendo os valores de x e y separados
    for c in range(len(matriz)):
        x.append(matriz[c][0])
        y.append(matriz[c][1])

    # Pega os valores de x e y para montagem do grafico
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

    # Mostra o grafico
    plt.show()

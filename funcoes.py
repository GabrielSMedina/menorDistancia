import random


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


def calcula_dist():
    pass


def gera_grafico():
    pass

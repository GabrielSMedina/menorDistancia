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


if __name__ == '__main__':
    print('Main')
    matriz = gerar_matriz(100)
    print(matriz)


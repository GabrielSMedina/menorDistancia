import funcoes


if __name__ == '__main__':
    # Gera uma matriz aleatoria
    matriz = funcoes.gerar_matriz(100)

    # Mostra essa matriz
    print(matriz)

    # Define um ponto arbitrario
    ponto = [24, 52]

    # 
    distancia, menor_ponto = funcoes.calcula_dist(matriz, ponto)
    distancia = round(distancia, 2)
    print(f'A menor distancia vale {distancia}, e seu ponto no grafico cartesiano é {menor_ponto}')

    funcoes.gera_grafico(matriz, menor_ponto, ponto)


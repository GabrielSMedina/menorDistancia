import funcoes


if __name__ == '__main__':
    # Pegando valores para o algoritmo
    tamanho, x, y = funcoes.inputs()

    # Gera uma matriz aleatoria
    matriz = funcoes.gerar_matriz(tamanho)

    # Mostra essa matriz
    print(matriz)

    # Define um ponto arbitrario
    ponto = [x, y]

    # Descobre qual o ponto que esta mais perto de nosso ponto arbitrario e retorna a distancia
    distancia, menor_ponto = funcoes.calcula_dist(matriz, ponto)
    # Arredonda a distancia para duas casas decimais
    distancia = round(distancia, 2)

    # Informe a distancia
    print(f'A menor distancia vale {distancia}, e seu ponto no grafico cartesiano é {menor_ponto}')

    # Gera um grafico para visualização dos pontos
    funcoes.gera_grafico(matriz, menor_ponto, ponto)


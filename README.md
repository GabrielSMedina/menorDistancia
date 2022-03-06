# Menor Distancia

Um algoritmo que recebe um ponto arbitrário e busca qual é o ponto
mais próximo dentre os gerados aleatoriamente pelo próprio código.
Este projeto foi feito com o intuito de estudar um pouco mais da linguagem,
utilizando conceitos como números aleatórios, matrizes e geração de gráficos.

## Como Utilizar:

- Instale a biblioteca matplotlib para poder utilizar a função de
geração de gráficos;
- Execute o arquivo main para rodar o código;
- Informe os parâmetros pedidos para o funcionamento do algoritmo.

## Tecnologia Utilizada:
Neste projeto foi utilizado o python como linguagem principal e algumas bibliotecas
pertencentes a ele para resolver operações matemáticas, criar números
aleatórios e gerar gráficos para termos um output de dados mais visual.

## Matemática do algoritmo:

Foi Utilizado a fórmula de Pitágoras para calcular a distância entre os diferentes pontos até o ponto arbitrario, como mostrado no
rascunho abaixo:

![grafico](https://user-images.githubusercontent.com/42703913/156940845-67fddbfd-0ffd-47eb-9137-d01acd2a9eac.jpg)

Para adaptar essas informações para codigo, foi pensado a seguinte solução:
```
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
```

Onde 'dist' é a variavel que armazenará a menor distância encontrada

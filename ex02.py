"""Faça uma função que receba como parâmetro o número de lados de um polígono e:
- Se o número de lados for igual a 3, escrever TRIÂNGULO.
- Se o número de lados for igual a 4, escrever QUADRILÁTERO.
- Se o número de lados for igual a 5, escrever PENTÁGONO.
- Se o número de lados for diferente de 3, 4 ou 5, escrever VALOR INVÁLIDO"""""

def conta_lados(numero):
    if numero == 3:
        print("É Triangulo ")
    elif numero == 4:
        print("É Quadrilatero ")
    elif numero == 5:
        print("É Pentagono ")
    else:
        print("Valor invalido. ")


lados = int(input("Informe a quantidade de lados do poligono:"))
conta_lados(lados)




"""Escreva um programa para solicitar as notas de duas provas. Faça uma função que receba as duas 
notas por parâmetro e exibe a mensagem “Você foi Aprovado!” ou “Você foi Reprovado!”. Considere 
6.0 a média mínima para aprovação."""

def aprov_reprov(prova1, prova2):
    if (prova1 + prova2) / 2 >= 6:
        print("Aprovado!")
    else:
        print("Reprovado")


a = float(input("Informe a nota da primeira prova: "))
b = float(input("Informe a nota da segunda nota: "))
resultado = aprov_reprov(a, b)


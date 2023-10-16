"""Escreva um programa que leia o raio de um círculo e faça duas funções: uma função chamada area
que calcula e retorna a área do círculo e outra função chamada perimetro que calcula e retorna o
perímetro do círculo. Utilize as fórmulas abaixo
Área = π * r2
Perímetro = π * 2 * r"""

def calc_area(pi, raio):
    area = pi * (raio*raio)
    return area

def calc_perimetro(pi, raio):
    perimetro = pi * 2 * raio
    return perimetro



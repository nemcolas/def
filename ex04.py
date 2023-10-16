"""Faça uma função que recebe um número inteiro por parâmetro e retorna True se for par e False se
for ímpar."""

def e_par (numero):
    if numero % 2 == 0:
        return True
    else:
        if numero % 2 != 0:
            return False

a = int(input("Informe um número: "))
print(e_par(a))

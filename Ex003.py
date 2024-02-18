"""Exercício 003 – Somando dois números: Crie um programa que leia dois números
e mostre a soma entre eles."""

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
soma = n1+n2
print('A soma entre eles é: {}'.format(soma))

#ou então:
print('A soma entre {} e {} é igual a {}. '.format(n1, n2, soma))

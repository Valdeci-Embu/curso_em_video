"""Exercício 006 – Dobro, Triplo, Raiz Quadrada: Crie um algoritmo que leia um número
e mostre o seu dobro, triplo e raiz quadrada."""
n = int(input('Digite um número: '))
d = 2*n
t = 3*n
r = float(n**(1/2))
print('Você digitou o número {}. Seu dobro é {}, seu triplo é {} e a raiz quadrada é {:.2f}.'.format(n, d, t, r))

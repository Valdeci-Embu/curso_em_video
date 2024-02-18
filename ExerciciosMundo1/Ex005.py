"""Exercício 005 – Antecessor e Sucessor: Faça um programa que leia um número inteiro
e mostre na tela o seu sucessor e seu antecessor."""
n = int(input("Digite um número inteiro: "))
a = int(n-1)
s = int(n+1)
print('Analizando o número {}, seu sucessor é {} e o antecessor é {}.'.format(n, s, a))

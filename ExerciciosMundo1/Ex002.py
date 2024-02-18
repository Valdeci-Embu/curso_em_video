"""Exercício 002 – Respondendo ao Usuário: Faça um programa que leia o nome de uma pessoa
e mostre uma mensagem de boas-vindas."""

nome = input('Digite seu nome: ')
print('É um prazer conhecê-lo,', nome)

#ou então
print('É um prazer conhecê-lo, {}'.format(nome))

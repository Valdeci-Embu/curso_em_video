"""Exercício 004 – Dissecando uma Variável: Faça um programa que leia algo pelo teclado
e mostre o seu tipo primitivo e todas as informações possíveis sobre ele."""
a = input("Digite algo:")
print('O tipo primitivo de {} é {}.'.format(a, type(a)))
print('Só tem espaços?', a.isspace())
print('É um número?', a.isnumeric())
print('É alfabético?', a.isalpha())
print('É alfa-numérico?', a.isalnum())
print('Está em maiúscula?', a.isupper())
print('Está em minúsculas?', a.islower())
print('Está capitalizada?', a.istitle())

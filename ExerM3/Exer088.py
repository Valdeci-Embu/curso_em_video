"""
EXERCÍCIO 088:
Palpites para a Mega Sena: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta.
"""
from random import randint
from time import sleep
print("=" * 29)
print('=' *3, "Palpites da Mega Sena", "=" *3)
print("=" * 29)
quant = int(input("Quantos jogos eu devo fazer? "))
lista = list()
jogos = list()
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('=' * 4, f'Exibindo {quant} palpites', "=" * 4)
print(f"Os números sorteados foram:")
for i, l in enumerate(jogos):
    print(f"Jogo {i+1}: {l}")
    sleep(1)
print('=*' * 4, 'Boa Sorte', '=*' * 4)

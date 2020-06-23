from random import choice
from time import time

# Adiciona os nomes à lista
nome = input("Digite todos os nomes a serem adicionados (separe-os por espaços): ").strip().lower()
lista = nome.split()

print("Os nomes a serem sorteados são:", lista)

# Sorteia os nomes
while len(lista) > 0:
    nome = input("Sortear para: ").strip().lower()
    sort = nome
    i = time()
    while sort == nome:
        # Se só sobrar uma pessoa e o nome dessa pessoa levanta SystemError
        if time() > i + 1 and len(lista) == 1:
            raise SystemError('Erro: o único papel restante é o seu nome')
        sort = choice(lista)
    print(sort)
    lista.remove(sort)

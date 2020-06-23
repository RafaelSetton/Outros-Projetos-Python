from random import randint
from time import time

acertos = 0
erros = 0
input("Pressione Enter para iniciar.")
print("Quando você quiser parar, digite um valor não numérico.")
inicio = time()
while True:
    num = randint(1, 101)
    try:
        resposta = int(input(f"³√{num**3}"))
    except ValueError:
        fim = time()
        print("Saindo.")
        print(f"Você acertou {int((acertos / (acertos + erros)) * 100)}% das questões!")
        print(f"Você respondeu um total de {acertos + erros} questões em {int(fim - inicio)} segundos!")
        break
    if resposta == num:
        print("Parabéns!")
        acertos += 1
    else:
        print(f"Você errou, a resposta correta é {num}. Continue tentando")
        erros += 1

# Questões: 10 + 14 + 14 + 16  = 54
# Tempo:    68 + 74 + 63 + 92  = 297
# seg/Qst:  6,8  5,3  4,5  5,7 = 5,5

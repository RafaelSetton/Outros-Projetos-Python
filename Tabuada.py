from random import randint
from time import time

tabuada = int(input("Qual tabuada você quer treinar? "))
acertos = 0
erros = 0
print("Quando você quiser parar, digite um valor não numérico.")
inicio = time()
while True:
    tabuada2 = randint(0, tabuada + 1)
    try:
        resposta = int(input(f"{tabuada} X {tabuada2} = "))
    except ValueError:
        fim = time()
        print("Saindo.")
        print(f"Você acertou {int((acertos / (acertos + erros)) * 100)}% das questões!")
        print(f"Você respondeu um total de {acertos + erros} questões em {int(fim - inicio)} segundos!")
        break
    if resposta == tabuada * tabuada2:
        print("Parabéns!")
        acertos += 1
    else:
        print(f"Você errou, a resposta correta é {tabuada * tabuada2}. Continue tentando")
        erros += 1

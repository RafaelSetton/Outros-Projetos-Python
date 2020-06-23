soma = 0
for i in range(1, 101):
    produto = float(input(f"{i}° produto: R$ "))
    soma += produto
    if produto == 0:
        break
print(f"Total: R$ {soma:.2f}")
pago = int(input("Total pago: R$ "))
troco = pago - soma
print(f"Troco: R$ {troco:.2f}")

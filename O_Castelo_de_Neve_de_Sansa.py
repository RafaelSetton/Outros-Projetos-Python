NK = input("N, K: ").split(', ')
alturas = [1]
print('h1: 1')
for i in range(2, int(NK[0])):
    alturas.append(int(input(f"h{i}: ")))
print(f'h{NK[0]}: 1')
alturas.append(1)
# Verifica se há duas alturas iguais
for index, altura in enumerate(alturas):
    try:
        if altura == alturas[index+1]:
            result = 'Ugly'
    except IndexError:
        pass
picos = 0
# Verifica quantos picos existem
for index, altura in enumerate(alturas):
    if index == 0 or index == int(NK[0])-1:
        pass
    elif alturas[index-1] < altura > alturas[index+1]:
        picos += 1
if picos == int(NK[1]):
    result = 'Beautiful'
else:
    result = 'Ugly'

print(result)

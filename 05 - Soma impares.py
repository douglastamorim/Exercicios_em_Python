soma: int = 0
i = int

print("Digite dois numeros: ")
x = int(input())
y = int(input())

if x > y:
    troca = x
    x = y
    y = troca

for i in range(x+1,y):
    if i % 2 != 0:
        soma = soma + i
print(f"Soma dos Impares = {soma}")
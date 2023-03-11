
n = int(input("Insira o número que deseja começar o fibonacci:"))

ultimo = 1
penultimo = 1

if (n == 1) or (n == 2):
    print("1")
else: 
    count = 3
    while count <= n:
        soma = ultimo + penultimo
        penultimo = ultimo
        ultimo = soma
        count += 1
    print(soma)
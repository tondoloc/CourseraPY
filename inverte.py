
lista = []
while True:
    numero = int(input("Digite um número inteiro: "))
    if (numero != 0):
        lista.append(numero)
    else:
        break

for i in lista[::-1]:
    print (i)

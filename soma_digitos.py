n = int(input("Digite um número inteiro: "))

soma = 0

while (n != 0):
	dig = n % 10
	soma = soma + dig	
	n = n // 10
	
	
print(soma)


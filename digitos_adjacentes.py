n = int(input("Digite um número inteiro: "))

adjac = False
dig_a = n % 10
n = n // 10

while (n > 0 and not adjac):
	dig_d = n % 10
	n = n // 10
	if (dig_d == dig_a):
		adjac = True
	dig_a = dig_d
if adjac:
	print("sim")
else:
	print("não")

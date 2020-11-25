num = int(input("Digite um número: "))

aux1 = num % 5
aux2 = num % 3
if (aux1 == 0) and (aux2 == 0):
	print("FizzBuzz")
else:
	print("%s"%(num))
	

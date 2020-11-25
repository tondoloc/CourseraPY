import math

num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))
num3 = int(input("Digite um número: "))
num4 = int(input("Digite um número: "))

dist = math.sqrt((num1 - num2)**2 + (num3 - num4)**2)

if (dist >= 10):
	print("longe")
else:
	print("perto")
	

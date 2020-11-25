import math

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

delta = (b**2) - (4*a*c)

if delta < 0:
	print("esta equação não possui raízes reais")
else:
	if delta == 0:
		x = -b/(2*a)
		print("a raiz desta equação é %f."%(x))
	else:
		if delta > 0:
			x_l = (-(b) + math.sqrt(delta))/(2*a)
			x_dl = (-(b) - math.sqrt(delta))/(2*a)
			if (x_l < x_dl):
				print("as raízes da equação são %f e %f"%(x_l,x_dl))
			else:
				print("as raízes da equação são %f e %f"%(x_dl,x_l))

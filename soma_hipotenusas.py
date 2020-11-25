def calcular_hipotenusa(a, b):
    return ((a*a) + (b*b))

def soma_hipotenusas(n):
    c = 1
    soma = 0
    while (c <= n):
        cd = (c*c)       
        a = 1
        b = 1
        while (a < n):
            while (b < n):
                if (cd == calcular_hipotenusa(a, b)):
                    soma = soma + c
                    a = n
                    break
                b = b + 1
            a = a + 1
            b = a
        c = c + 1
  
    return soma

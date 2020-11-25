def primo(x):

    i = 1
    cont = 0
    while i <= x:
        if x % i == 0:
            cont = cont + 1
        i = i + 1
    if cont > 2:
        return False
    else:
        return True

def n_primos(n):

    #n = int(input("Digite um número inteiro: "))

    if (n < 2):
        return 0
    elif (n == 2):
        return 1
    else:
        contador = 1
        while (n > 2):
            if (primo(n)):
                contador = contador + 1
            n = n - 1
        return contador

    return 0

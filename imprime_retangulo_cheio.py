
largura = int(input("digite a largura:"))
altura = int(input("digite a altura:"))

linha = 0
coluna = 0

while linha < altura:
    while coluna < largura:
        print("#", end="")
        coluna = coluna + 1
    print()

    linha = linha+1
    coluna = 0
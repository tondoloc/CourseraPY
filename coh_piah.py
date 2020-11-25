import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    som = 0

    for i in range(0, 6):

        som = som + (abs(as_a[i] - as_b[i]))

        similaridade = som / 6

    return similaridade
    pass

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    lista_de_palavras = separa_palavras(texto)
    numero_total_de_palavra = len(lista_de_palavras)
    lista_sentenca = separa_sentencas(texto)
    numero_total_sentencas = len(lista_sentenca)
    
    tamanho_medio_de_palavra = numero_total_de_caractere_palavra(texto) / numero_total_de_palavra
    relacao_Type_Token = numero_total_de_palavras_diferentes(texto) / numero_total_de_palavra
    razao_Hapax_Legomana = numero_total_de_palavras_unicas(texto) / numero_total_de_palavra

    tamanho_medio_de_sentenca = numero_total_de_caractere_sentenca(texto) / numero_total_sentencas
    complexidade_de_sentenca = numero_total_de_frases(texto) / numero_total_sentencas
    tamanho_medio_de_frase = numero_total_de_caractere_frase(texto) / numero_total_de_frases(texto)
    return [tamanho_medio_de_palavra, relacao_Type_Token, razao_Hapax_Legomana, tamanho_medio_de_sentenca, complexidade_de_sentenca, tamanho_medio_de_frase]
    pass

def numero_total_de_caractere_palavra(texto):
    num_car = 0
    lista_sentenca = separa_sentencas(texto)[:]
    lista_frases = []
    for i in lista_sentenca:
        lista_frases = lista_frases + separa_frases(i)
    lista_palavras = []
    for i in lista_frases:
        lista_palavras = lista_palavras + separa_palavras(i)
    for i in lista_palavras:
        num_car =  num_car + len(i)
    return num_car

def numero_total_de_palavras_diferentes(texto):
    lista_sentenca = separa_sentencas(texto)
    lista_frases = []
    for i in lista_sentenca:
        lista_frases = lista_frases + separa_frases(i)
        lista_palavras = []
    for i in lista_frases:
        lista_palavras = lista_palavras + separa_palavras(i)
    return n_palavras_diferentes(lista_palavras)

def numero_total_de_palavras_unicas(texto):
    lista_sentenca = separa_sentencas(texto)
    lista_frases = []
    for i in lista_sentenca:
        lista_frases = lista_frases + separa_frases(i)
        lista_palavras = []
    for i in lista_frases:
        lista_palavras = lista_palavras + separa_palavras(i)
    return n_palavras_unicas(lista_palavras)

def numero_total_de_caractere_sentenca(texto):
    num_car = 0
    lista_sentenca = separa_sentencas(texto)[:]
    lista_frases = []
    for i in lista_sentenca:
        num_car = num_car + len(i)
    return num_car

def numero_total_de_frases(texto):
    lista_sentenca = separa_sentencas(texto)
    num_fras = 0
    for i in lista_sentenca:
        num_fras = num_fras + len(separa_frases(i))
    return num_fras

def numero_total_de_caractere_frase(texto):
    num_car = 0
    lista_sentenca = separa_sentencas(texto)[:]
    lista_frases = []
    for i in lista_sentenca:
        lista_frases += separa_frases(i)
    for i in lista_frases:
        num_car = num_car + len(i)
    return num_car

def avalia_textos(textos, ass_cp):
    lista_similaridade = []
    for i in range(0, len(textos)):
        ass_texto = calcula_assinatura(textos[i])
        grau_similaridade = compara_assinatura(ass_texto, ass_cp)
        lista_similaridade.append(grau_similaridade)
    texto_doente = lista_similaridade.index((min(lista_similaridade))) + 1
    print ("O autor do texto %d está infectado com COH-PIAH" %(texto_doente))
    return texto_doente
 
def main():
    assinatura_cp = le_assinatura() 
    textos_lidos = le_textos() 
    avalia_textos(textos_lidos, assinatura_cp)

main()

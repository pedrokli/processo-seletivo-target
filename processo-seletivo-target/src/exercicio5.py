

def pede_palavra():
    palavra = input("Qual a palavra? ")
    quantidade_de_letras = len(palavra)

    palavra_invertida = []


    while( quantidade_de_letras > 0):
        palavra_invertida += palavra[quantidade_de_letras - 1]
        quantidade_de_letras = quantidade_de_letras - 1

    palavra_invertida = "".join(palavra_invertida)
    return palavra_invertida

print("A palavra invertida é " + pede_palavra())
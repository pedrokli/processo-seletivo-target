

def pede_palavra():
    palavra = input("Qual a palavra?")
    quantidade_de_letras = len(palavra)

    palavra_invertida = []


    while( quantidade_de_letras > 0):
        palavra_invertida += palavra[quantidade_de_letras - 1]
        quantidade_de_letras = quantidade_de_letras - 1

    print("A palavra invertida é: ", palavra_invertida)

pede_palavra()

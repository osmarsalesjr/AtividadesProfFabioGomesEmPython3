
def main():
    print(">> Conversor de CONSOANTES para # <<\n")
    
    frase = input("Escreva uma frase: ")
    vogais = "aeiou"
    nova_frase = ""

    for i in range(len(frase)):
        if frase[i].lower() not in vogais.lower() and frase[i] != " ":
            nova_frase += "#"
        else:
            nova_frase += frase[i]


    print("Resultado: '%s' " % nova_frase)


if __name__ == '__main__':
    main()
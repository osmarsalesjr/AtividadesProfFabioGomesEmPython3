def main():
    print(">>AS PALAVRAS DE UMA FRASE SEM ESPACOS <<\n")

    frase = input("Escreva uma frase: ")
    nova_frase = ""

    for i in range(len(frase)):
        if frase[i] == " ":
            nova_frase += ""
        else:
            nova_frase += frase[i]

    print(nova_frase)


if __name__ == '__main__':
    main()
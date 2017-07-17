def main():
    print(">>AS PALAVRAS DE UMA FRASE SEM ESPACOS <<\n")

    frase = input("Escreva uma frase: ")
    nova_frase = ""

    for i in range(len(frase)):
        nova_frase += frase[i] * 2

    print(nova_frase)


if __name__ == '__main__':
    main()
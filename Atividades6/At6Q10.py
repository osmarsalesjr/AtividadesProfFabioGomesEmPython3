
def main():
    palavra = input("Digite uma palavra: ")
    inverso = ""

    for letra in reversed(palavra):
        inverso += letra

    print("Original: %s || Invertido: %s" % (palavra, inverso))

    if palavra == inverso:
        print("Palavra e Palindroma!")
    else:
        print("Palavra nao e Palindroma!")



if __name__ == '__main__':
    main()
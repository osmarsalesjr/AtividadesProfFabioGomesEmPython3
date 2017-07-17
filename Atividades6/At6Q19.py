
def main():
    print(">> Converter Binary to Decimal <<")

    binario = input("Digite um Numero Binario: ")
    binario_auxiliar = ""

    decimal = 0

    for letra in reversed(binario):
        binario_auxiliar += letra
    
    for i in range(len(binario_auxiliar)):
        if binario_auxiliar[i] == "1":
            decimal += 2 ** i

    print("O binario %s corresponde a %d no sistema decimal." % (binario, decimal))


if __name__ == '__main__':
    main()
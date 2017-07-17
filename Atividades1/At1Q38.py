
def main():
    numerador1 = int(input("Digite o numerador da fração 1: "))
    denominador1 = valida_denominador()

    numerador2 = int(input("Digite o numerador da fração 2: "))
    denominador2 = valida_denominador()

    calcula_fracoes(numerador1, numerador2, denominador1, denominador2)


def valida_denominador():
    numero = int(input("Digite o denominador da fração 1: "))
    while numero <= 0:
        print("Escolha uma valor diferente de zero.")
        numero = int(input("Digite o denominador da fração: "))
    return numero


def calcula_fracoes(numerador1, numerador2, denominador1, denominador2):
    if denominador1 == denominador2:
        resultado = numerador1 + numerador2
        print (resultado,"/",denominador1)
    else:
        mmc = denominador1 * denominador2
        numerador1 = numerador1 * (mmc / denominador1)
        numerador2 = numerador2 * (mmc / denominador2)
        resultado = int(numerador1 + numerador2)
        print (resultado,"/",mmc)


if __name__ == "__main__":
    main()

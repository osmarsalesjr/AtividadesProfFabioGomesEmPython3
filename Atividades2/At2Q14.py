
def main():

    numero1 = int(input("Digite o primeiro numero: "))
    numero2 = int(input("Digite o segundo numero: "))
    numero3 = int(input("Digite o terceiro numero: "))
    numero4 = int(input("Digite o quarto numero: "))
    numero5 = int(input("Digite o quinto numero: "))

    media = (numero1 + numero2 + numero3 + numero4 + numero5) / 5

    print("\nMedia: %.2f." % media)

    print("\n>>> Numeros Acima da Media <<<")
    if numero1 > media:
        print(numero1)

    if numero2 > media:
        print(numero2)

    if numero3 > media:
        print(numero3)

    if numero4 > media:
        print(numero4)

    if numero5 > media:
        print(numero5)





if __name__ == '__main__':
    main()
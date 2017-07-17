def main():
    numero1 = float(input("Digite o primeiro numero: "))
    numero2 = float(input("Digite o segundo numero: "))
    numero3 = float(input("Digite o terceiro numero: "))
    print("A média é igual a ", calcula_media(numero1, numero2, numero3), ".")


def calcula_media(number1,number2,number3):
    media = (number1+number2+number3)/3
    return media

if __name__ == '__main__':
    main()
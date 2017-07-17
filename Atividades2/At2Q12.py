
def main():
    numero = int(input("Digite um numero: "))
    print(impar_ou_par(numero))


def impar_ou_par(numero):
    if numero % 2 == 1:
        return "Numero e impar!"
    else:
        return "Numero e par!"


if __name__ == '__main__':
    main()
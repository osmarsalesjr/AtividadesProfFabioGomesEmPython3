from random import randint

def main():
    print(">> Digite o numero gerado pelo sistema entre 0 e 100 <<")
    aleatorio = randint(0, 100)
    print(aleatorio)
    numero = int(input("Digite o próximo numero: "))
    while verifica_numero(aleatorio, numero) == False:
        numero = int(input("Tente outro numero: "))


def verifica_numero(aleatorio, numero):
    if numero > aleatorio:
        print("Maior.")
    elif numero < aleatorio:
        print("Menor.")
    else:
        print("Parabens, Voce Conseguiu!!!")
        return True
    return False


if __name__ == "__main__":
    main()

def main():
    numero = int(input("Digite um Número: "))
    escreva_soma(numero)


def escreva_soma(numero):
    soma = 0
    for i in range(1, numero):
        soma = soma + i
    print("Soma %d"% soma)


if __name__ == "__main__":
    main()

def main():
    numero = int(input("Digite um valor limite: "))
    escreva_fracoes(numero)


def escreva_fracoes(numero):
    print("S = ")
    for i in range(1, numero+1):
        if i % 2 == 0:
            print(" + 1/%d" % i)
        else:
            print(" - 1/%d" % i)


if __name__ == "__main__":
    main()

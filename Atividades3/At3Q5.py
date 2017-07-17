
def main():
    numero = int(input("Digite um numero: "))
    print(fatorial(numero))

def fatorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * fatorial(numero - 1)


if __name__ == "__main__":
    main()
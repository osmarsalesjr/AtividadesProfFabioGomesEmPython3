
def main():
    maior = 0
    qtd = int(input("Digite a quantidade: "))
    for i in range(qtd):
        numero = int(input("Digite um numero: "))
        if numero > maior:
            maior = numero
            print(maior)
    print(maior)


if __name__ == "__main__":
    main()
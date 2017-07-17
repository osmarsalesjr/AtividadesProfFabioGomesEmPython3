
def main():
    numero1 = int(input("Digite o primeiro numero: "))
    numero2 = int(input("Digite o próximo numero: "))
    print("{} * {} = {}".format(numero1, numero2, escreva_produto(numero1, numero2)))

def escreva_produto(numero1, numero2):
    produto = 0
    for i in range(numero2):
        produto = produto + numero1
    return produto


if __name__ == "__main__":
    main()

def main():
    print(">>>> Sequência de Fibonacci <<<<")
    numero = int(input("Digite um número: "))
    mostre_quadrado(numero)

def mostre_quadrado(numero):
    sequencia = 0
    for i in range(1, numero):
        sequencia = sequencia + (i+1)
        print(sequencia)


if __name__ == "__main__":
    main()
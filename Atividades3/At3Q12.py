
def main():
    soma = 0
    qtd  = int(input("Digite a quantidade numeros: "))
    for i in range(qtd):
        numero = int(input("Digite um numeros: "))
        soma = soma + numero
    media = soma / qtd
    print("Soma dos Números: %d" % soma)
    print("Media dos Números: %.2f" % media)


if __name__ == "__main__":
    main()
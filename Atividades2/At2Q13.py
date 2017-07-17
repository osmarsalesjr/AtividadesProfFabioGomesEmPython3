
def main():
    numero = int(input("Digite um numero: "))
    maior, menor = numero, numero
    for i in range(4):
        numero = int(input("Digite um numero: "))
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

    print("Maior numero e: %d e o menor e %d." % (maior, menor))



if __name__ == '__main__':
    main()
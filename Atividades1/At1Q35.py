def main():
    number = int(input("Digite um valor de 4 números: "))
    print("Soma dos dígitos é: ", soma_digitos(number))

def soma_digitos(numero):
    resto, soma = 0,0
    while numero>0:
        resto = numero%10
        numero = (numero-resto)/10
        soma = soma+resto
    return soma

if __name__ == '__main__':
    main()
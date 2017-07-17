
def main():
    numero = valida_numero()
    if valida_primo(numero) == True:
        print("Numero e Primo!")
    else:
        print("Numero Nao e Primo!")


def valida_numero():
    while True:
        numero = int(input("Digite um numero: "))
        if numero <= 0 and numero >= 100:
            print("Por favor digite uma valor acima de 0 e menor que 100.")
        else:
            break
    return numero


def valida_primo(numero):
    contador = 0
    for i in range(1, numero + 1):
        if numero % i != 0:
            continue
        else:
            contador += 1
    if contador == 2:
        return True
    else:
        return False


if __name__ == '__main__':
    main()
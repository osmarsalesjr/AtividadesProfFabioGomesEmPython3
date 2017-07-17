def verifica_maior(valor1, valor2, valor3):
    maior = 0
    if (valor1>valor2 and valor1>valor3) or (valor1==valor2 and valor1>valor3):
        maior = valor1
    elif (valor2>valor1 and valor2>valor3) or (valor2==valor3 and valor2>valor1):
        maior = valor2
    else:
        maior = valor3
    return maior


def main():
    numero_1 = int(input("Digite um número: "))
    numero_2 = int(input("Digite um número: "))
    numero_3 = int(input("Digite um número: "))
    print(verifica_maior(numero_1, numero_2, numero_3), " foi o Maior Número Digitado.")


if __name__ == "__main__":
    main()
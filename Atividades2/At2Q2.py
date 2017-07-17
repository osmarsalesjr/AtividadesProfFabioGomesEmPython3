def verifica_numeros(valor1, valor2):
    if valor1==valor2:
        print("Números São Iguais.")
    elif valor1>valor2:
        print(valor1," é Maior e ",valor2," é Menor.")
    else:
        print(valor2, " é Maior e ", valor1, " é Menor.")


def main():
    numero_1 = int(input("Digite um número: "))
    numero_2 = int(input("Digite um número: "))
    verifica_numeros(numero_1, numero_2)


if __name__ == "__main__":
    main()
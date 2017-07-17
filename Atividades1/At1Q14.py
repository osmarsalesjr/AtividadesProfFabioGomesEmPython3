
def main():
    print(">>> Media Ponderada de Notas <<<")

    nota1 = float(input("Digite o valor da primeira nota: "))
    peso1 = int(input("Digite o valor de peso dessa nota: "))

    nota2 = float(input("Digite o valor da segunda nota: "))
    peso2 = int(input("Digite o valor de peso dessa nota: "))

    nota3 = float(input("Digite o valor da terceira nota: "))
    peso3 = int(input("Digite o valor de peso dessa nota: "))

    media_ponderada = ((nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3)) / (peso1 + peso2 + peso3)

    print("A média ponderada é ", media_ponderada, ".")


if __name__ == '__main__':
    main()

def main():
    print(">>> Área de um Triângulo <<<")

    base = float(input("Digite o valor da base do triângulo: "))
    altura = float(input("Digite o valor da altura: "))
    area = (base * altura) / 2
    print("A altura desse triângulo é ", area, "m².")


if __name__ == '__main__':
    main()
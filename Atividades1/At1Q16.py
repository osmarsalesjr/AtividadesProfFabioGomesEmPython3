def main():
    lado_quadrado = float(input("Digite o valor do lado do quadrado para obter sua area: "))
    print("A area desse quadrado é ", calcula_area(lado_quadrado), "u².")


def calcula_area(valor_lado):
    area = valor_lado ** 2
    return area

if __name__ == '__main__':
    main()
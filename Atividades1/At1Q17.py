
def main():
    base_triangulo = float(input("Valor da base do triangulo: "))
    altura_triangulo = float(input("Valor da altura do triangulo: "))
    print("A area do triangulo é ", area_triangulo(base_triangulo, altura_triangulo), "u².")


def area_triangulo(base,height):
    area = (base*height)/2
    return area

if __name__ == '__main__':
    main()
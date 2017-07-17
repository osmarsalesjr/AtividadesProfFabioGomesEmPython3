def main():
    primeiro_lado = valida_lado()
    segundo_lado = valida_lado()
    terceiro_lado = valida_lado()

    if (primeiro_lado + segundo_lado) < terceiro_lado or (primeiro_lado + terceiro_lado) < segundo_lado or (segundo_lado + terceiro_lado) < primeiro_lado:
        print("Valores Nao Formam um Triangulo!")
    elif primeiro_lado == segundo_lado and segundo_lado == terceiro_lado:
        print("Valores Formam um Triangulo Equilatero!")
    elif primeiro_lado == segundo_lado or primeiro_lado == terceiro_lado or segundo_lado == terceiro_lado:
        print("Valores Formam um Triangulo Isosceles!")
    else:
        print("Valores Formam um Triangulo Escaleno!")

def valida_lado():
    while True:
        lado = int(input("Digite um valor de lado para o triangulo: "))
        if lado <= 0:
            print("Por favor digite uma valor acima de 0.")
        else:
            break
    return lado


if __name__ == '__main__':
    main()
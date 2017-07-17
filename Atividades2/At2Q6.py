

def main():
    primeiro_angulo = valida_algulo()
    segundo_angulo = valida_algulo()
    terceiro_angulo = valida_algulo()
    soma = primeiro_angulo + segundo_angulo + terceiro_angulo

    if soma != 180:
        print("Valores Nao Formam um Triangulo!")
    elif primeiro_angulo < 90 and segundo_angulo < 90 and terceiro_angulo < 90:
        print("Valores Forma Triangulo Acutangulo!")
    elif primeiro_angulo == 90 or segundo_angulo == 90 or terceiro_angulo == 90:
        print("Valores Forma Triangulo Retangulo!")
    else:
        print("Valores Forma Triangulo Obtusangulo!")



def valida_algulo():
    while True:
        angulo = int(input("Digite o valor angulo do triangulo: "))
        if angulo <= 0:
            print("Por favor digite uma valor acima de 0º.")
        else:
            break
    return angulo


if __name__ == '__main__':
    main()
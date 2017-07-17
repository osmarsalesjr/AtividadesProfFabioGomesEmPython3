def main():
    print(">> Veja a soma de um número pelo seu inverso. <<")
    number = int(input("Escreva um numero de 3 dígitos: "))
    print("A diferença ent1re (ABC+CBA) é: ", calcula_soma(number), ".")


def calcula_soma(numero):
    numero_inverso = str(numero)[2]+str(numero)[1]+str(numero)[0]
    numero_inverso = int(numero_inverso)
    soma = numero+numero_inverso
    return soma

if __name__ == '__main__':
    main()
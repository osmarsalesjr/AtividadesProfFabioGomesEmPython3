def ordem_crescente(valor1, valor2, valor3):
    if (valor1 < valor2 and valor1 < valor3 and valor2 < valor3) or (valor1 == valor2 and valor2 < valor3) or (valor2 == valor3 and valor1 < valor2):
        print(valor1, valor2, valor3)
    elif (valor1 < valor2 and valor1 < valor3 and valor3 < valor2) or (valor1 == valor3 and valor3 < valor2):
        print(valor1, valor3, valor2)
    elif (valor2 < valor1 and valor2 < valor3 and valor1 < valor3) or (valor1 == valor2 and valor2 < valor3) or (valor1 == valor3 and valor2 < valor3):
        print(valor2, valor1, valor3)
    elif (valor2 < valor1 and valor2 < valor3 and valor3 < valor1) or (valor2 == valor3 and valor3 < valor1):
        print(valor2, valor3, valor1)
    elif (valor3 < valor1 and valor3 < valor2 and valor1 < valor2) or (valor1 == valor2 and valor3 < valor2) or (valor1 == valor3 and valor3 < valor2):
        print(valor3, valor1, valor2)
    else:
        print(valor3, valor2, valor1)

def main():
    numero_1 = int(input("Digite um número: "))
    numero_2 = int(input("Digite um número: "))
    numero_3 = int(input("Digite um número: "))
    ordem_crescente(numero_1, numero_2, numero_3)


if __name__ == "__main__":
    main()
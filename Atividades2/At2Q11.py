
def main():
    numero1 = int(input("Digite o primeiro numero: "))
    numero2 = int(input("Digite o segundo numero: "))
    numero3 = int(input("Digite o terceiro numero: "))
    opcao = int(input("Digite um valor de 1 a 3: "))

    if opcao == 1:
        print(numero1)
    elif opcao == 2:
        print(numero2)
    elif opcao == 3:
        print(numero3)
    else:
        print("A opcao digitada não possui valor.")




if __name__ == '__main__':
    main()

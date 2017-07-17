
def main():
    print(">>> Progressão Geométrica <<<")
    a_zero = int(input("Digite o valor de Ao: "))
    razao = int(input("Digite o valor da razão: "))
    limite = int(input("Digite um valor limite: "))
    escreva_valores(a_zero, razao, limite)

def escreva_valores(a_zero, razao, limite):
    valor = 0
    for i in range(a_zero, limite):
        a_zero *= razao
        if a_zero < limite:
            print(a_zero)
        else:
            break


if __name__ == "__main__":
    main()

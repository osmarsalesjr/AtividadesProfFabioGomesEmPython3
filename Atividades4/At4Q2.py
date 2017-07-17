
def main():
    numero_1 = int(input("Digite um número: "))
    numero_2 = int(input("Digite um número: "))
    mmc = calcula_mmc(numero_1, numero_2)
    print("O mmc é igual a %d"%mmc)

def calcula_mmc(numero1, numero2):
    resultado = (numero1 * numero2) / calcula_mdc(numero1, numero2)
    return resultado


def calcula_mdc(numero1, numero2):
    if numero2 == 0:
        return numero1
    return calcula_mdc(numero2, numero1%numero2)



if __name__ == "__main__":
    main()

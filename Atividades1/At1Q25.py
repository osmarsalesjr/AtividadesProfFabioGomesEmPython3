

def main():
    valor_metros = int(input("Digite um valor em M: "))
    print("Esse valor equivale a ", calcula_kilometros(valor_metros), "km e ", calcula_metros(valor_metros), "m.")


def calcula_kilometros(valor_m):
    return int(valor_m/1000)

def calcula_metros(valor_m):
    return valor_m%1000

if __name__ == '__main__':
    main()
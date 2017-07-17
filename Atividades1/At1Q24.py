
def main():
    valor_em_metros = float(input("Digite um valor em M: "))
    print("Esse valor equivale a ", calcula_cm(valor_em_metros), "cm.")


def calcula_cm(valor_m):
    centimetros = valor_m*100
    return centimetros

if __name__ == '__main__':
    main()
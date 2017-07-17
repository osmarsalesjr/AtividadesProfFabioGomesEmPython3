def main():
    kilogramas = float(input("Digite um valor em Kg: "))
    print("Esse valor equivale a ", calcula_gramas(kilogramas), "g.")


def calcula_gramas(valor_kg):
    return valor_kg*1000

if __name__ == '__main__':
    main()
def main():
    temperatura_celsius = int(input("Digite uma temperatura em ºC: "))
    print("Essa temperatura equivale a ", calcula_temperatura(temperatura_celsius), "ºF.")


def calcula_temperatura(temper_em_c):
    temper_em_f = ((temper_em_c*9)+160)/5
    return temper_em_f

if __name__ == '__main__':
    main()
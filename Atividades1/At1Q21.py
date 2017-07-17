
def main():
    temperatura_fahrenheit = int(input("Digite uma temperatura em ºF: "))
    print("Essa temperatura equivale a ", calcula_temperatura(temperatura_fahrenheit), "ºC.")


def calcula_temperatura(temper_em_f):
    temper_em_celsius = ((temper_em_f*5)-160)/9
    return temper_em_celsius

if __name__ == '__main__':
    main()
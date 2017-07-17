
def main():
    kilometros = float(input("Digite um valor em KM: "))
    print("Esse valor equivale a ", calcula_metros(kilometros), "ms.")

def calcula_metros(valor_km):
    return valor_km*1000

if __name__ == '__main__':
    main()
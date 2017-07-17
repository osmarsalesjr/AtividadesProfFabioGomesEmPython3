
def main():
    limite_inferior = int(input("Digite um valor de inicio: "))
    limite_superior = int(input("Digite um valor limite: "))
    numero_pares(limite_inferior, limite_superior)

def numero_pares(limite_inferior, limite_superior):
    print(">>>> Relação de Numeros Pares %d e %d <<<<" % (limite_inferior, limite_superior))
    for i in range(limite_inferior, limite_superior):
        if i % 2 == 0:
            print(">> %d"%i)


if __name__ == "__main__":
    main()
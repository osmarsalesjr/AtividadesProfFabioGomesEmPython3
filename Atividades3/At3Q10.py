
def main():
    numero  = int(input("Digite um numeros: "))
    limite_inferior = int(input("Digite um valor de inicio: "))
    limite_superior = int(input("Digite um valor limite: "))
    escreva_multiplos(limite_inferior, limite_superior)

def escreva_multiplos(limite_inferior, limite_superior):
    print(">>>> Relação de Multiplos entre %d e %d <<<<" % (limite_inferior, limite_superior))
    for i in range(limite_inferior + 1, limite_superior):
        if i % 2 != 0:
            print(">> %d"%i)


if __name__ == "__main__":
    main()

def main():
    numero  = int(input("Digite um numeros: "))
    limite_inferior = int(input("Digite um valor de inicio: "))
    limite_superior = int(input("Digite um valor limite: "))
    escreva_multiplos(limite_inferior, limite_superior, numero)

def escreva_multiplos(limite_inferior, limite_superior, numero):
    print(">>>> Relação de Multiplos de %d entre %d e %d <<<<" % (numero, limite_inferior, limite_superior))
    for i in range(limite_inferior, limite_superior):
        if i % numero == 0:
            print(">> %d"%i)


if __name__ == "__main__":
    main()
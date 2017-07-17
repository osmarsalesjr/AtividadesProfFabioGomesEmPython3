
def main():
    limite_inferior = int(input("Digite um numero para ponto de partida: "))
    limite_superior = int(input("Digite o valor limite: "))
    numeros_primos(limite_inferior, limite_superior)


def numeros_primos(num_inferior, num_superior):
    print(">>>> Numeros primos: ")
    for i in range(num_inferior, num_superior):
        contador = 0
        for j in range(1, i+1):
            if i % j == 0:
                contador = contador + 1
        if contador == 2:
            print(">> %d"%i)




if __name__ == "__main__":
    main()
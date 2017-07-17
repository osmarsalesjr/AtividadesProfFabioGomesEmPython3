def escreve_divisores(numero):
    if numero <= 0:
        print("FIM")
    else:
        for i in range(1, numero+1):
            if numero % i == 0:
                print(i)
        main()



def main():
    numero = int(input("Digite um número: "))
    escreve_divisores(numero)

if __name__ == "__main__":
    main()
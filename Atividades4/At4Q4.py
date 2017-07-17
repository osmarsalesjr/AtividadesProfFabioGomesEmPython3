def efetua_divisoes(numero):
    return int(numero/2)

def main():
    numero = int(input("Digite um número: "))
    while efetua_divisoes(numero)!= 0:
        numero = efetua_divisoes(numero)
    print(numero)



if __name__ == "__main__":
    main()
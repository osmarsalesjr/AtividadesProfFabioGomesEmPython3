def verifica_digitos(numero):
    print(numero%10)
    print(int(numero/10))
    if numero%10 == int(numero/10):
        print("Digitos são iguais.")
    else:
        print("Digitos não são iguais.")

def valida_numero(numero):
    while numero < 10 or numero > 100:
        numero = int(input("Digite um número: "))
    return numero

def main():
    numero = valida_numero(0)
    verifica_digitos(numero)



if __name__ == "__main__":
    main()
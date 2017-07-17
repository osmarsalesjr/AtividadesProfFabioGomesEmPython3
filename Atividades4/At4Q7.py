
def main():
    print(">>> Digite Números até ser Igual ao Primeiro.")
    numero1 = int(input("Digite o primeiro numero: "))
    numero2 = int(input("Digite o próximo numero: "))
    while verifica_numero(numero1, numero2) == False:
        numero2 = int(input("Digite o próximo numero: "))
    print("Você digitou um número igual ao primeiro!!!\nTerminado.")

def verifica_numero(numero1, numero2):
    if numero1 == numero2:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
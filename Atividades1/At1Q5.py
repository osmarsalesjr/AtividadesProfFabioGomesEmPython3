
def main():
    num = int(input("Digite um Número de 3 dígitos: "))
    print("A soma dos dígitos é igual: ", soma_digitos(num))

def soma_digitos(number):
    number = str(number)
    soma = int(number[0])+int(number[1])+int(number[2])
    return soma

if __name__ == "__main__":
    main()
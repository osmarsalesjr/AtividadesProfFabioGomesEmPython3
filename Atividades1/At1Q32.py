def main():
    print(">> Veja a diferença de um número pelo seu inverso. <<")
    number = int(input("Escreva um numero de 3 dígitos: "))
    print("A diferença entre (ABC-CBA) é: ", calcula_diferenca(number), ".")

def calcula_diferenca(numero):
    numero_inverso = str(numero)[2]+str(numero)[1]+str(numero)[0]
    numero_inverso = int(numero_inverso)
    diferenca = numero-numero_inverso
    return diferenca

if __name__ == '__main__':
    main()
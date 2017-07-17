
def main():
    print(">> Calculando Expressões <<\nD = (R+S)/2; R = (A+B)² e S = (B+C)²")
    print("Vamos obter os valores para A, B e C...")
    valor_a = int(input("Valor para A: "))
    valor_b = int(input("Valor para B: "))
    valor_c = int(input("Valor para C: "))
    print("O resultado da expressão D = (R+S)/2; R = (A+B)² e S = (B+C)² é:\n",calcula_expressao(valor_a, valor_b, valor_c))


def calcula_expressao(numero_a, numero_b, numero_c):
    numero_r = pow((numero_a+numero_b),2)
    numero_s = pow((numero_b+numero_c),2)
    numero_d = (numero_r+numero_s)/2
    return numero_d

if __name__ == "__main__":
    main()
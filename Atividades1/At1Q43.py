

def main():
    print(">> Calcule os Valores de X e Y <<")
    print("Equação: ax+by = c ; dx+ey = f ; x = ((c*e)-(b*f))/((a*e)-(b*d)) e y = ((a*f)-(c*d))/((a*e)-(b*d))")
    print("Agora vamos precisar dos valores para a, b, c, d, e, e f.")
    a = int(input("Digite um Valor para A: "))
    b = int(input("Digite um Valor para B: "))
    c = int(input("Digite um Valor para C: "))
    d = int(input("Digite um Valor para D: "))
    e = int(input("Digite um Valor para E: "))
    f = int(input("Digite um Valor para F: "))
    calcula_equacao(a, b, c, d, e, f)

def calcula_equacao(a, b, c, d, e, f):
    x = ((c*e)-(b*f))/((a*e)-(b*d))
    y = ((a*f)-(c*d))/((a*e)-(b*d))
    print("Os valores encontrados são: X = %.2f"%x," e Y = %.2f"%y,".")


if __name__ == "__main__":
    main()

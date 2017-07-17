def main():
    salario_bruto = float(input("Digite um valor do salário: "))
    salario_liquido = salario_bruto + (salario_bruto * 0.25)
    print("O salário líquido com 25% de aumento é R$ ", salario_liquido, " Reais.")


if __name__ == '__main__':
    main()
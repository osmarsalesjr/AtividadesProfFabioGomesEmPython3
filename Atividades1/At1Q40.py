

def main():
    anos_fumante = int(input("Há quantos você fuma: "))
    numero_diario_cigarros = int(input("Quantos cigarros POR DIA: "))
    preco_carteira_cigarros = float(input("Qual o valor da Carteira de Cigarros? R$ "))
    print("O custo total é de R$ %.2f"%custo_por_fumar(anos_fumante,numero_diario_cigarros,preco_carteira_cigarros)," reais.")

def custo_por_fumar(anos_fumo,cigarros_dia,preco_carteira):
    total_dias = anos_fumo*365
    total_cigarros = cigarros_dia*total_dias
    custo_total = (total_cigarros/20)*preco_carteira
    return custo_total


if __name__ == "__main__":
    main()
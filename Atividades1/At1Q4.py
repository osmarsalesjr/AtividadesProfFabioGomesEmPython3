def main():
    valor_em_dolar = float(input("Digite um valor em dólares($): "))
    print("Esse Valor corresponde a R$ ", dolar_para_real(valor_em_dolar), " Reais.")


def dolar_para_real(valor_dolar):
    valor_em_reais = valor_dolar*3.49
    return valor_em_reais

if __name__ == "__main__":
    main()
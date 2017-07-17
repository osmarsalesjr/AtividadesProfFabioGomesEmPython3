import math

def main():
    print(">>Calcule a Previsão de seus Investimentos <<")
    continuar = 1
    while continuar == 1:
        investimento = float(input("Quanto você pretende investir ao mês em R$: "))
        taxa_juros = int(input("Qual a taxa de juros a ser aplicada ao mês em %: "))
        calcula_investimento(investimento, taxa_juros)
        continuar = int(input("Deseja calcular mais um ano? 1- SIM | 2- NÃO "))
    print("Terminado.")


def calcula_investimento(investimento, taxa):
    saldo_investido = 0
    taxa = taxa/100
    for i in range(1, 13):
        saldo_investido = investimento + (saldo_investido * pow((1+taxa), i))
    print("Saldo de Investimento Após um Ano: R$ %.2f"%saldo_investido," reais.")


if __name__ == "__main__":
    main()
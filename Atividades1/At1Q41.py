
def main():
    preco_fabrica = float(input("Qual o custo de fábrica do carro: R$ "))
    valor_carro = preco_carro_novo(preco_fabrica)
    print("O valor do carro novo será de R$ %.2f"%valor_carro," reais.")

def preco_carro_novo(custo_fabrica):
    custo_total = custo_fabrica+((custo_fabrica*0.28)+(custo_fabrica*0.45))
    return custo_total



if __name__ == "__main__":
    main()
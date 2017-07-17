
def main():
    nome = input("Qual o Nome do Produto? ")
    while nome != "FIM" or nome != "fim":
        preco_unit = float(input("Qual o valor unitário do produto em R$? "))
        quantidade = int(input("Qual a quantidade desejada? "))
        custo = calcula_valor(preco_unit, quantidade)
        print("O valor total da compra de ", nome, " é de R$ %.2f" % custo, " reais.")
        print("PARA CONTINUAR DIGITE O NOME DE UM NOVO PRODUTO OU 'FIM' PARA ENCERRAR")
        nome = input("Qual o nome do produto? ")
    print("Terminado.")

def calcula_valor(preco_unico, quantidade):
    if quantidade > 50:
        custo_total = (preco_unico * quantidade) - (preco_unico * quantidade * 0.25)
    elif quantidade >= 21 and quantidade <= 50:
        custo_total = (preco_unico * quantidade) - (preco_unico * quantidade * 0.20)
    elif quantidade >= 11 and quantidade <= 20:
        custo_total = (preco_unico * quantidade) - (preco_unico * quantidade * 0.10)
    else:
        custo_total = preco_unico * quantidade

    return custo_total


if __name__ == "__main__":
    main()
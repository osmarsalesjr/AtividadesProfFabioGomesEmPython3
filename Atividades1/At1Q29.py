
def main():
    qtd_meses = int(input("Quantidade de tempo em meses: "))
    print("Valor é equivalente a ", calcula_anos(qtd_meses), " anos e ", calcula_meses(qtd_meses), " meses.")

def calcula_anos(total_meses):
    return int(total_meses/12)

def calcula_meses(total_meses):
    return total_meses%12

if __name__ == '__main__':
    main()
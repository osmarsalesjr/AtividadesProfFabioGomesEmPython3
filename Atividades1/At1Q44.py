
def main():
    print("Digite a Quantidade de Latão que Você precisa e saiba como obtê-lo.")
    peso_latao = float(input("Digite a quantidade de latao que voce deseja obter: "))
    calcula_componentes(peso_latao)



def calcula_componentes(qtd_latao):
    qtd_cobre = qtd_latao*0.70
    qtd_zinco = qtd_latao*0.30
    print("Para obter %.2f"%qtd_latao,"kg de Latão você precisará de %.2f"%qtd_cobre,"kg de Cobre e %.2f"%qtd_zinco,"kg de Zinco.")



if __name__ == "__main__":
    main()

def main():
    data = input("Digite uma da e veja o mes por extenso: DD MM AAAA (Somente numeros)--> ")
    mes = data[3 : 5]

    if int(mes) >= 1 and int(mes) <= 12:
        data = data[0 : 3] + escreva_data(mes) + data[5 : len(data)]
        print(data)

    else:
        print("Mes esta incorreto.")


def escreva_data(mes):
    meses = ["Janeiro", "Fevereiro", "Marco", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro",
             "Novembro", "Dezembro"]
    for i in range(len(meses)):
        if int(mes) == i + 1:
            return meses[i]


if __name__ == '__main__':
    main()
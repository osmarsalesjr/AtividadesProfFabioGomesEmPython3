def main():
    qtd_dias = int(input("Quantidade de dias: "))
    print("Esse quantidade equivale a ", calcula_semanas(qtd_dias), "semanas e ", calcula_dias(qtd_dias), " dia(s).")


def calcula_semanas(days):
    return int(days/7)

def calcula_dias(days):
    return days%7

if __name__ == '__main__':
    main()
def main():
    qtd_dias = int(input("Digite uma quantidade de dias: "))
    print("O tempo estimado é de ", calcula_anos(qtd_dias), " anos, ", calcula_meses(qtd_dias), " meses e ",
          calcula_dias(qtd_dias), " dias.")


def calcula_anos(days):
    years = int(days/365)
    return years

def calcula_meses(days):
    months = int((days-(calcula_anos(days)*365))/30)
    return months

def calcula_dias(days):
    days_remaining = (days-(calcula_anos(days)*365))-(calcula_meses(days)*30)
    return days_remaining

if __name__ == '__main__':
    main()
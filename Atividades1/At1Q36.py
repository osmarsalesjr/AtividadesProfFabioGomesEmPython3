def main():
    years = int(input("Digite a quantidade de anos: "))
    months = int(input("Digite a quantidade de meses: "))
    days = int(input("Digite a quantidade de dias: "))
    print("O total estimado de dias é ", calcula_dias(years, months, days))



def calcula_dias(anos,meses,dias):
    total_dias = (anos*365)+(meses*30)+dias
    return total_dias


if __name__ == '__main__':
    main()
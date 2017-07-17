def main():
    qtd_minutos = int(input("Quantidade de tempo em minutos: "))
    print("Esse tempo equivale a ", calcula_dias(qtd_minutos), " dia(s), ", calcula_horas(qtd_minutos), " hora(s) e ",
          calcula_minutos(qtd_minutos), " minuto(s).")


def calcula_dias(total_minutes):
    days = int(total_minutes/1440)
    return days

def calcula_horas(total_minutes):
    hours = int((total_minutes - (calcula_dias(total_minutes) * 1440))/60)
    return hours

def calcula_minutos(total_minutes):
    minutos = (total_minutes-(calcula_dias(total_minutes)*1440)-calcula_horas(total_minutes)*60)
    return minutos

if __name__ == '__main__':
    main()
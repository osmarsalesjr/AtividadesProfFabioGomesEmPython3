
def main():
    qtd_horas = int(input("Quantidade de tempo em horas: "))
    print("Esse tempo equivale a ", calcula_semanas(qtd_horas), " semanas, ", calcula_dias(qtd_horas), " dias e ",
          calcula_horas(qtd_horas), " horas.")



def calcula_semanas(total_hours):
    weeks = int(total_hours/168)
    return weeks

def calcula_dias(total_hours):
    days = int((total_hours-(calcula_semanas(total_hours)*168))/24)
    return days

def calcula_horas(total_hours):
    hours = (total_hours-(calcula_semanas(total_hours)*168))-(calcula_dias(total_hours)*24)
    return hours

if __name__ == '__main__':
    main()
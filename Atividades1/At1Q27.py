
def main():
    qtd_segundos = int(input("Quantidade de tempo em segundos: "))
    print("O valor corresponde a ", calcula_hours(qtd_segundos), "hrs, ", calcula_minutes(qtd_segundos), " mns e ",
          calcula_seconds(qtd_segundos), "s.")



def calcula_hours(seconds):
    hours = int(seconds/3600)
    return hours

def calcula_minutes(seconds):
    minutes = (seconds-(calcula_hours(seconds)*3600))/60
    return int(minutes)

def calcula_seconds(seconds):
    seconds_remaining = (seconds-(calcula_hours(seconds)*3600))-(calcula_minutes(seconds)*60)
    return seconds_remaining

if __name__ == '__main__':
    main()
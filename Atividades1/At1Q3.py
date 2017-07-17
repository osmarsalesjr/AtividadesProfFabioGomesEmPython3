
def main():
    minutos = int(input("Digite um valor em minutos: "))
    print("Os valores calculados correspondem a um total de ", calcula_horas(minutos), " horas e ", calcula_minutos(minutos), " minutos.")


def calcula_horas(minutes):
    hours = int(minutes/60)
    return hours

def calcula_minutos(minutes):
    minutes_remaining = minutes%60
    return minutes_remaining

if __name__ == "__main__":
    main()
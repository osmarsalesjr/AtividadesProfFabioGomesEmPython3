
def main():
    horas = int(input("Digite um valor em horas: "))
    minutos = int(input("Digite um valor em minutos: "))
    print("Os valores calculados correspondem a um total de ", calcula_minutos(horas, minutos), " minutos.")


def calcula_minutos(hours,minutes):
    total_minutes = (hours*60)+minutes
    return total_minutes


if __name__ == "__main__":
    main()

def main():
    horario = input("Digite a hora exata em (HH:MM:SS) ")

    horario = horario[0 : 2] + " hora(s), " + horario[3 : 5] + " minuto(s) e " + horario[6 : 8] + " segundo(s)."

    print(horario)




if __name__ == '__main__':
    main()
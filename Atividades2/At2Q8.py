
def main():
    dia_atual = int(input("DIA ATUAL: "))
    mes_atual = int(input("MES ATUAL: "))
    ano_atual = int(input("ANO ATUAL: "))

    numero_dias_atuais = ((ano_atual * 365) + (mes_atual * 30)) + dia_atual

    dia_nascimento = int(input("DIA DE NASCIMENTO: "))
    mes_nascimento = int(input("MES DE NASCIMENTO: "))
    ano_nascimento = int(input("ANO DE NASCIMENTO: "))

    numero_dias_nascimento = ((ano_nascimento * 365) + (mes_nascimento * 30)) + dia_nascimento

    print("\nDias até a data de nascimento: %d dias.\nDias ate a data de hoje: %d dias." % (numero_dias_nascimento, numero_dias_atuais))
    print("Dias entre data de nascimento e a de hoje: %d dias." % (numero_dias_atuais - numero_dias_nascimento))

    total_anos = (numero_dias_atuais - numero_dias_nascimento) / 365

    print("\nIdade igual a %d anos." % total_anos)


if __name__ == '__main__':
    main()
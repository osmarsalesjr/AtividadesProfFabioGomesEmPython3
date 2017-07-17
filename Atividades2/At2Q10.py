
def main():
    dia = int(input("DIA: "))
    mes = int(input("MES: "))
    ano = int(input("ANO: "))
    if valida_data(dia, mes, ano) == True:
        print("DATA ESTA VALIDA!")
    else:
        print("DATA NAO ESTA VALIDA!")


def valida_data(dia, mes, ano):
    valido = True
    if (dia <= 0 or dia > 31 or mes <= 0 or mes > 12) or (dia == 30 and mes == 2):
        valido = False
    if dia >= 31 and (mes == 2 or mes == 4 or mes == 6 or mes == 9 or mes == 11):
        valido = False
    if dia == 29 and mes == 2 and (ano % 4 != 0 or (ano % 100 == 0 and ano % 400 != 0)):
        valido = False
    return valido

if __name__ == '__main__':
    main()

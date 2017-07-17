
def main():
    valor = float(input("Qual o Valor a Sacar em R$? "))
    conta_notas(valor)

def conta_notas(valor):
    notas_cem, notas_cinquenta, notas_vinte, notas_dez = 0, 0, 0, 0
    notas_cinco, notas_dois, notas_um = 0, 0, 0

    while valor >= 100:
        valor = valor - 100
        notas_cem = notas_cem + 1

    while valor >= 50:
        valor = valor - 50
        notas_cinquenta = notas_cinquenta + 1

    while valor >= 20:
        valor = valor - 20
        notas_vinte = notas_vinte + 1

    while valor >= 10:
        valor = valor - 10
        notas_dez = notas_dez + 1

    while valor >= 5:
        valor = valor - 5
        notas_cinco = notas_cinco + 1

    while valor >= 2:
        valor = valor - 2
        notas_dois = notas_dois + 1

    notas_um = int(valor)

    print(">> Quantidade de notas a serem recebidas: ")
    print("Notas de R$ 100: %d\nNotas de R$ 50: %d\nNotas de R$ 20: %d"%(notas_cem, notas_cinquenta, notas_vinte))
    print("Notas de R$ 10: %d\nNotas de R$ 5: %d\nNotas de R$ 1: %d"%(notas_dez, notas_cinco, notas_um))



if __name__ == '__main__':
    main()
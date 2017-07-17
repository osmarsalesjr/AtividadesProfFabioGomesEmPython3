def verifica_iguais(valor1, valor2, valor3):
    qtd_iguais = 0
    if valor1==valor2:
        qtd_iguais = qtd_iguais+1
    if valor1==valor3:
        qtd_iguais = qtd_iguais+1
    if valor2==valor3:
        qtd_iguais = qtd_iguais+1
    if qtd_iguais==1:
        qtd_iguais = qtd_iguais+1
    return qtd_iguais


def main():
    numero_1 = int(input("Digite um número: "))
    numero_2 = int(input("Digite um número: "))
    numero_3 = int(input("Digite um número: "))
    print("Existem ",verifica_iguais(numero_1, numero_2, numero_3)," números iguais.")


if __name__ == "__main__":
    main()
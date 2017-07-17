def main():
    print(">> Conversor de binários em decimal <<")
    numero_binario = input("Digite um valor binário de 4 algarismos: ")
    print("Esse valor equivale a ", conversor_bin_to_dec(numero_binario), " na base decimal.")


def conversor_bin_to_dec(num_bin):
    numero_decimal = 0
    valor_bin = num_bin[3] + num_bin[2] + num_bin[1] + num_bin[0]
    for i in range(4):
        if valor_bin[i] == "1":
            numero_decimal = numero_decimal + (2 ** i)
    return numero_decimal


if __name__ == '__main__':
    main()

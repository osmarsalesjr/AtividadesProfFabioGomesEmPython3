
def main():
    frase = input("Digite uma frase: ")
    nova_frase = ""

    for i in range(len(frase)):
        nova_frase += reescreva_frase(frase[i])

    print("\n\nFrase reescrita:\n%s" % nova_frase)



def reescreva_frase(caracter):
    novo_caracter = caracter
    digitos = ["_zero_", "_um_", "_dois_", "_tres_", "_quatro_", "_cinco_", "_seis_", "_sete_", "_oito_", "_nove_"]

    for i in range(len(digitos)):
        if caracter == str(i):
            novo_caracter = digitos[i]
            break

    return novo_caracter



if __name__ == '__main__':
    main()
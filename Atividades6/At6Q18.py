
def main():
    frase = input("Digite uma frase: ")
    texto_a_substituir = input("Que fragmento da frase voce deseja alterar: ")
    texto_a_incluir = input("Qual o texto a ser atribuido a frase: ")

    nova_frase = frase.replace(texto_a_substituir, texto_a_incluir)

    print("Alteracao Realizada com sucesso:\n%s" % nova_frase)



if __name__ == '__main__':
    main()
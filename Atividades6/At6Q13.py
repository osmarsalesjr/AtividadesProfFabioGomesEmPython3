
def main():
    nome = input("Nome Completo: ")
    iniciais = ""

    for i in range(len(nome)):
        if i == 0:
            iniciais += nome[i] + ". "
        if nome[i] == " " and nome[0 : i].count(" ") < nome.count(" ") - 1:
            iniciais += nome[i + 1 : i + 2] + ". "

    for i in range(len(nome)):
        if nome[0 : i].count(" ") == nome.count(" "):
            ultimo_nome = nome[i : len(nome)]
            break

    print("Autor: %s, %s" % (ultimo_nome, iniciais), end="")



if __name__ == '__main__':
    main()

def main():
    nome = input("Nome Completo: ")

    for i in range(len(nome)):
        if nome[0: i].count(" ") == 1:
            primeiro_nome = nome[0 : i - 1]
            nome_auxliar = nome[i + 1: len(nome)]
            break

    for i in range(len(nome)):
        if nome_auxliar[0 : i].count(" ") == nome_auxliar.count(" "):
            ultimo_nome = nome_auxliar[i : len(nome_auxliar)]
            break

    print("Passageiro: %s / %s." % (ultimo_nome, primeiro_nome))



if __name__ == '__main__':
    main()
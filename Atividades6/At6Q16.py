
def main():
    nome = input("Digite um nome: ")

    diagonal(nome)


def diagonal(nome):
    for i in range(len(nome)):
        if i == 0:
            print(nome[0 : i + 1])
        else:
            print((" " * i) + nome[i])


if __name__ == '__main__':
    main()
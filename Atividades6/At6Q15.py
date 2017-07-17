
def main():
    nome = input("Digite um nome: ")

    vertical(nome)


def vertical(nome):
    for i in range(len(nome)):
        print(nome[0 : i + 1])


if __name__ == '__main__':
    main()
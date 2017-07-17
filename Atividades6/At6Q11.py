
def main():
    texto = input("Digite um texto qualquer: ")
    qtd_palavras = texto.count(" ") + 1

    print("O texto digitado possui %d palavras." % qtd_palavras)


if __name__ == '__main__':
    main()

def main():
    words_no_e, words = 0, 0

    palavras = open("words.txt")

    for linha in palavras:
        palavra = linha.strip()

        if 'e' not in palavra:
            print(palavra)
            words_no_e = words_no_e + 1

        words = words + 1

    print("Percentual de palavras sem a letra E: %.1f %%" % ((words_no_e/words) * 100))



if __name__ == '__main__':
    main()



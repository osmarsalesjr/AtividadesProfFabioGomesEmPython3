
def main():
    palavras = open("words.txt")

    for palavra  in palavras:
       if len(palavra) > 20:
           print(palavra.strip())

if __name__ == '__main__':
    main()
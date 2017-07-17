
def main():

    verbo = input("Digite um verbo regular terminacao ER: ")

    pessoas = ["Eu", "Tu", "Ele(a)", "Nos", "Vos", "Eles(as)"]
    conjugacoes = ["eio", "es", "e", "emos", "eis", "eem"]

    print(">> Conjulgacao <<<\n")

    for i in range(len(conjugacoes)):
        print("%s   %s%s" % (pessoas[i], verbo[0 : len(verbo) - 2], conjugacoes[i]))



if __name__ == '__main__':
    main()

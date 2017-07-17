
def main():
    continuar = 1

    while continuar == 1:
        nome = input("Nome Completo: ")
        login = gere_login(nome)
        print("O seu login de usuario e: %s" % login)

        continuar = int(input("\n\nCadastrar outro usuario? 1 - SIM / 2 - NAO\n"))



def gere_login(nome):
    iniciais = ""

    for i in range(len(nome)):
        if i == 0:
            iniciais += nome[i].lower()
        if nome[i] == " ":
            iniciais += nome[i + 1].lower()
    login = iniciais + "@login.com"
    return login



if __name__ == '__main__':
    main()
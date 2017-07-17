
def main():
    senha = input("Digite uma senha com '*' entre os caracteres: ")
    if "*" in senha:
        print("Senha cadastrada esta valida!")
    else:
        print("Senha cadastrada nao esta valida!")



if __name__ == '__main__':
    main()
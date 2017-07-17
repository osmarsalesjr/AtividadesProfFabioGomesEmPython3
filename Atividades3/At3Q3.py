
def main():
    a0 = int(input("Digite o valor de inicial: "))
    limite = int(input("Digite um valor limite: "))
    razao = int(input("Digite a razao: "))
    for i in range(a0, limite, razao):
        print(i)


if __name__ == "__main__":
    main()
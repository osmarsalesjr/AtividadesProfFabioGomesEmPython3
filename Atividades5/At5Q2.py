
def main():
    a = [int(i) for i in input("Digite numeros para essa lista: ").split()]

    for i in range(len(a)):
        repetido = False
        if a.count(a[i]) > 1:
            repetido = True
            break


    if repetido == True:
        print("Ha numeros repetidos")
    else:
        print("Nao ha numeros repetidos")



if __name__ == '__main__':
    main()
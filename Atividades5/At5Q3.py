
def main():
    a = [int(i) for i in input("Digite os numeros da lista A: ").split()]
    b = [int(i) for i in input("Digite os numeros da lista B: ").split()]

    c = a + b

    print("A + B = ", c)


if __name__ == '__main__':
    main()
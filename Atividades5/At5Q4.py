
def main():
    a = [int(i) for i in input("Digite os numeros da lista A: ").split()]
    b = [int(i) for i in input("Digite os numeros da lista B: ").split()]

    c = a + b
    d = []
    for i in range(len(a)):
        if a[i] in b:
            d.append(a[i])

    print("A + B = ", c, "\nA Intercessao B = ",d)


if __name__ == '__main__':
    main()
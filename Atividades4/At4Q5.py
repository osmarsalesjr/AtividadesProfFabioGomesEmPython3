
def main():
    numerador = int(input("Numerador: "))
    denominador = int(input("Denominador: "))
    while denominador >= 2:
        print("{} / {} = {}".format(numerador, denominador, efetua_divisoes(numerador, denominador)))
        numerador = efetua_divisoes(numerador, denominador)
        denominador = denominador - 1


def efetua_divisoes(numerador, denominador):
    return int(numerador/denominador)


if __name__ == "__main__":
    main()
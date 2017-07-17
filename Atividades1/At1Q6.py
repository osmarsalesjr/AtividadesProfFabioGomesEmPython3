
def main():
    velocidade_em_km = float(input("Digite a Velocidade em KM/S: "))
    print("O valor de ", velocidade_em_km, "km/s corresponde a ", velocidade_ms(velocidade_em_km), "m/s.")


def velocidade_ms(vel_km):
    velocidade_em_ms = vel_km/3.6
    return velocidade_em_ms

if __name__ == '__main__':
    main()
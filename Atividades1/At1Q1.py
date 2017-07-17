
def main():
    velocidade_em_ms = float(input("Digite a Velocidade em M/S: "))
    print("O valor de ", velocidade_em_ms, "m/s corresponde a ", conversor_velocidade(velocidade_em_ms), "km/s.")


def conversor_velocidade(vel_ms):
    vel_km = vel_ms*3.6
    return vel_km


if __name__ == "__main__":
    main()

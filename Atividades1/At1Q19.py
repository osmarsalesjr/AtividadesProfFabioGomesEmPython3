import math

def main():
    raio_esfera = float(input("Valor do raio da esfera: "))
    print("O volume dessa esfera é ", volume_esfera(raio_esfera), "u³.")

def volume_esfera(valor_raio):
    volume = (4*3.14*(pow(valor_raio,3))/3)
    return volume

if __name__ == '__main__':
    main()
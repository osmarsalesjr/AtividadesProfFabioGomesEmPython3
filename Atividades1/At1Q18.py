
def main():
    raio_circunferencia = float(input("Valor do raio da circunferência: "))
    print("O comprimento dessa cincurferência é: ", comprimento_circunferencia(raio_circunferencia), ".")

def comprimento_circunferencia(valor_raio):
    comprimento = 2*3.14*valor_raio
    return comprimento

if __name__ == '__main__':
    main()
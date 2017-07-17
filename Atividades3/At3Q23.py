
def main():
    codigo = int(input("Código do Funcionário: "))
    horas_trabalhadas = int(input("Horas Trabalhadas do Funcionário: "))
    dependentes = int(input("Número de Dependentes do Funcionário: "))
    calcula_dados(codigo, horas_trabalhadas, dependentes)
    continuar = int(input("Verificar outro funcionario? 1 - SIM \ 2 - NÃO "))
    if continuar == 1:
        main()
    else:
        print("Terminado.")

def calcula_dados(codigo, horas_trabalhadas, dependentes):
    salario_bruto = ((horas_trabalhadas * 12.00) + (dependentes * 40.00))
    salario_liquido = salario_bruto - ((salario_bruto * 0.0085) + (salario_bruto * 0.05))
    imposto_inss = salario_bruto * 0.0085
    imposto_ir = salario_bruto * 0.05

    print(">>>>>>> Informações do Contra-Cheques <<<<<<<\n")
    print("Matricula: %d" % codigo)
    print("Salario Bruto: R$ %.2f reais." % salario_bruto)
    print("Salario Liquido: R$ %.2f reais." % salario_liquido)
    print("Descontos:\nINNS R$ %.2f reais.\nIR R$ %.2f reais." % (imposto_inss, imposto_ir))



if __name__ == "__main__":
    main()
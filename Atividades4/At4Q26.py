

def main():
    idade = int(input("Qual a Sua Idade? "))
    opiniao = int(input("Qual a sua opinião sobre o filme:\n1- Otimo | 2- Bom | 3- Regular | 4- Pessimo.\n"))
    total_entrevistados, idades_otimo, contador_otimo, contador_regular, entrevistados_bom = 0, 0 , 0, 0, 0
    while idade > 0:
        total_entrevistados = total_entrevistados + 1
        if opiniao == 1:
            idades_otimo = idades_otimo + idade
            contador_otimo = contador_otimo + 1
        if opiniao == 3:
            contador_regular = contador_regular + 1
        if opiniao == 2:
            entrevistados_bom = entrevistados_bom + 1
        idade = int(input("Qual a Sua Idade? "))
        opiniao = int(input("Qual a sua opinião sobre o filme:\n1- Otimo | 2- Bom | 3- Regular | 4- Pessimo.\n"))

    calcula_dados(total_entrevistados, idades_otimo, contador_otimo, contador_regular, entrevistados_bom)


def calcula_dados(toltal_entrevistados, idades_otimo, contador_otimo, contador_regular, entrevistados_bom):
    media_idade_op_otimo = idades_otimo/contador_otimo
    percentual_entrevistados_bom = (entrevistados_bom/toltal_entrevistados)*100
    print(">>>> Resultados <<<<")
    print("Média de Idade dos Entrevistado que Opinaram Otimo: %.2f"%media_idade_op_otimo)
    print("Quantidade de Pessoas que Opinaram Regular: ",contador_regular)
    print("Percentual de Pessoas que Opinaram Bom: %.2f"%percentual_entrevistados_bom,"%.")


if __name__ == "__main__":
    main()
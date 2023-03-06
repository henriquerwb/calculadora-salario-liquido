def calcular_aliquota(salario): #Função para calcular a aliquota de desconto do INSS.
    if salario == 1302:
        aliquota = 0.075
    elif salario > 1302 and salario <= 2571.29:
        aliquota = 0.09
    elif salario > 2571.29 and salario <= 3856.94:
        aliquota = 0.12
    elif salario > 3856.94:
        aliquota = 0.14
    else:
        aliquota = 0
    return aliquota

def calcular_inss(salario, aliquota):
    if salario == 1302:
        desconto = salario * aliquota
    elif salario > 1302 and salario <= 2571.29:
        desconto = (1302 * 0.075) + ((salario - 1302) * aliquota)
    elif salario > 2571.29 and salario <= 3856.94:
        desconto = (1302 * 0.075) + ((2571.29 - 1302) * 0.09) + ((salario - 2571.29) * aliquota)
    elif 3856.94 < salario <= 7507.49:
        desconto = (1302 * 0.075) + ((2571.29 - 1302) * 0.09) + ((3856.94 - 2571.29) * 0.12) + ((salario - 3856.94) * aliquota)
    elif salario > 7507.49:
        desconto = 828.39
    return desconto

def calcular_passagem(salario):
    calculo_passagem = salario * 0.06
    return calculo_passagem




def main():
    salario = float(input('Digite o  seu salário bruto: '))
    contador = 0
    while contador == 0:
        escolha_passagem = str(input('Possui o benefício de vale transporte? (S/N): ')).upper()
        if escolha_passagem == 'Y':
            valor_passagem = calcular_passagem(salario)
            contador = 1
        elif escolha_passagem == 'N':
            valor_passagem = 0
            contador = 1
        else:
            print('Opção inválida!')
            contador = 0
    outros_descontos = float(input('Digite outros descontos fora INSS e VT: '))
    desconto_inss = calcular_inss(salario, calcular_aliquota(salario))
    salario_liquido = salario - desconto_inss - valor_passagem - outros_descontos
    print(f'Seu salário líquido é {salario_liquido:.2f} R$ e o total de descontos é de {desconto_inss + valor_passagem + outros_descontos} R$.')




if __name__ == "__main__":
    main()
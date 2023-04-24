if __name__ == '__main__':
    nome = input('Qual o seu nome? ')
    salario_fixo = float(input('Quanto você recebe mensalmente? '))
    vendas = float(input('Quanto você lucrou com suas vendas esse mês? = '))

    comissao = vendas * 0.15
    salario_final = salario_fixo + comissao

    print(f"TOTAL = R$ {salario_final:.2f}")

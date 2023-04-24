if __name__ == '__main__':
    numero = int(input(' Qual o valor correspondente ao funcionário? = '))
    horas = int(input('Quantas horas trabalhadas você tem? '))
    valor_hora = float(input('Quanto vale sua hora trabalhada? '))

    salario = horas * valor_hora

    print("NUMBER =", numero)
    print("SALARY = $", "{:.2f}".format(salario))

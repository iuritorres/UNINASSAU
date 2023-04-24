if __name__ == '__main__':
    salary = float(input('Digite aqui o valor do seu salário = '))

    if salary <= 400:
        percent = 15
    elif salary <= 800:
        percent = 12
    elif salary <= 1200:
        percent = 10
    elif salary <= 2000:
        percent = 7
    else:
        percent = 4

    reajuste = salary * percent / 100
    novo_salary = salary + reajuste

    print(f"Novo salario: {novo_salary:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print(f"Em percentual: {percent} %")

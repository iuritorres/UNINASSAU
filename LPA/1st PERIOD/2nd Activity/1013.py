if __name__ == '__main__':
    a, b, c = input('Insira seus Valores para cálculo =  ').split()
    a, b, c = int(a), int(b), int(c)

    maior_ab = (a + b + abs(a - b)) / 2
    maior_abc = (maior_ab + c + abs(maior_ab - c)) / 2

    print(f"{maior_abc} EH o maior")

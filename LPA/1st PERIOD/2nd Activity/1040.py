if __name__ == '__main__':
    n1, n2, n3, n4 = map(float, input('Insira suas notas = ').split())

    mp = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1) / 10

    if mp >= 7.0:
        print(f"Average: {mp:.1f}\nAluno aprovado.")

    elif mp < 5.0:
        print(f"Average: {mp:.1f}\nAluno reprovado.")

    else:
        print(f"Average: {mp:.1f}\nAluno em exame.")
        exame = float(input())
        new_average = (mp + exame) / 2
        print(f"Nota do exame: {exame:.1f}")

        if new_average >= 5.0:
            print(f"Aluno aprovado.\nAverage final: {new_average:.1f}")

        else:
            print(f"Aluno reprovado.\nAverage final: {new_average:.1f}")

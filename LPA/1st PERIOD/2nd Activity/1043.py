if __name__ == '__main__':
    a, b, c = map(float, input('Insira os valores de A, B e C por favor = ').split())

    if a + b > c and a + c > b and b + c > a:
        perimeter = a + b + c
        print(f"Perimeter = {perimeter:.1f}")

    else:
        area = (a + b) * c / 2
        print(f"Area = {area:.1f}")

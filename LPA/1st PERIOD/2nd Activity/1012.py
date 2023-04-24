import math as mh

if __name__ == '__main__':
    a, b, c = map(float, input('Insira aqui seus respectivos valores de entrada A, B e C = ').split())

    triangulo = (a * c) / 2
    circulo = mh.pi * (c ** 2)
    trapezio = ((a + b) * c) / 2
    quadrado = b ** 2
    retangulo = a * b

    print("TRIANGULO: {:.3f}".format(triangulo))
    print("CIRCULO: {:.3f}".format(circulo))
    print("TRAPEZIO: {:.3f}".format(trapezio))
    print("QUADRADO: {:.3f}".format(quadrado))
    print("RETANGULO: {:.3f}".format(retangulo))

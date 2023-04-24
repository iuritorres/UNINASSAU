import math as mh

if __name__ == '__main__':
    x1, y1 = map(float, input('Insira seus eixos primários = ').split())
    x2, y2 = map(float, input('Insira seus exios secundários = ').split())

    distancia = mh.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    print('{:.4f}'.format(distancia))

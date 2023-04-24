if __name__ == '__main__':
    dist = int(input('Qual a distância que será percorrida? = '))
    comb = float(input('Quanto você gastou de Gasolina nesse trajeto? = '))

    consumo_medio = dist / comb

    print('{:.3f} km/l'.format(consumo_medio))

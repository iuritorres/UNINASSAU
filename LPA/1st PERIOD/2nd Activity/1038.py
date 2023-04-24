if __name__ == '__main__':
    code, amount = map(int, input('Insira aqui o que você deseja adquirir 1.Cachorro Quente - 2.X-Salada -  3.X-Bacon - 4.Torrada 5.Refrigerante ').split())

    if code == 1:
        preco = 4.00
    elif code == 2:
        preco = 4.50
    elif code == 3:
        preco = 5.00
    elif code == 4:
        preco = 2.00
    elif code == 5:
        preco = 1.50

    total = preco * amount

    print("Total: R$ {:.2f}".format(total))

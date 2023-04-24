import os
os.system('cls')

if __name__ == '__main__':
    tree = {
        'vertebrado': {
            'ave': {
                'carnivoro': 'aguia',
                'onivoro': 'pomba'
            },
            'mamifero': {
                'onivoro': 'homem',
                'herbivoro': 'vaca'
            }
        },

        'invertebrado': {
            'inseto': {
                'hematofago': 'pulga',
                'herbivoro': 'lagarta'
            },
            'analideo': {
                'hematofago': 'sanguessuga',
                'onivoro': 'minhoca'
            }
        }
    }

    bone = str(input('vertebrado ou invertebrado: ')).lower()
    kindof = str(input('ave, mamifero, inseto, analideo: ')).lower()
    feed = str(input('carnivoro, onivoro, herbivoro, hematofago: ')).lower()

    os.system('cls')
    print(tree[bone][kindof][feed])

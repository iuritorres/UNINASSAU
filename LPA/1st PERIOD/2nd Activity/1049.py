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

    while True:
        bone = str(input('bone: ')).lower()
        if bone not in tree:
            os.system('cls')
            print(f'Invalid option, you can only type: {list(tree.keys())}')
        
        else: break

    while True:
        kindof = str(input('kindof: ')).lower()
        if kindof not in tree[bone]:
            os.system('cls')
            print(f'Invalid option, you can only type: {list(tree[bone].keys())}')
        
        else: break

    while True:
        feed = str(input('feed: ')).lower()
        if feed not in tree[bone][kindof]:
            os.system('cls')
            print(f'Invalid option, you can only type: {list(tree[bone][kindof].keys())}')

        else:
            print(tree[bone][kindof][feed])
            break

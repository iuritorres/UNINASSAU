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

    current = 'bone'

    while True:
        if current == 'bone':
            bone = str(input('bone: ')).lower()

            if input('bone: ').lower() not in tree:
                os.system('cls')
                print(f'Invalid option, you can only type: {list(tree.keys())}')
            else:
                current = 'kindof'

        elif current == 'kindof':
            kindof = str(input('kindof: ')).lower()

            if kindof not in tree[bone]:
                os.system('cls')
                print(f'Invalid option, you can only type: {list(tree[bone].keys())}')
            else:
                current = 'feed'

        elif current == 'feed':
            feed = str(input('feed: ')).lower()

            if feed not in tree[bone][kindof]:
                os.system('cls')
                print(f'Invalid option, you can only type: {list(tree[bone][kindof].keys())}')
            else:
                break

    print(tree[bone][kindof][feed])

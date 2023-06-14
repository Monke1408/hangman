import random


words = ['хуй','член','пенис','моча']

a = random.choice(words)

def hangman(word):
    wrong = 0
    stages = ['',
              '______________      ',
              '|                   ',
              '|             |     ',
              '|             0     ',
              '|            /|\    ',
              '|            / \    ',
              '|                   '
              ]
    rleters = list(word)
    board = ['_']*len(word)
    win = False
    print('Добро пожаловать на казнь')


    while wrong < len(stages)-1:
        print('\n')
        msg = 'Ввидите букву:'
        otvet = input(msg)
        if otvet in rleters:
            cind = rleters.index(otvet)
            board[cind] = otvet
            rleters[cind] = '$'
        else:
            wrong += 1
        print((' '.join(board)))
        e = wrong + 1
        print('\n'.join(stages[0:e]))
        if '_' not in board:
            print("Ура победа!!! Загаданое слово было:")
            print('\n'.join(board))
            win = True
            break



    if win == False:

        print('\n'.join(stages[0:wrong]))

        print('Ну ты и лошок!!! Слово было {}'.format(word))



    
hangman(a)        
    

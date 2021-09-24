import random


def game():
    choice = input('Want to play again? y/n\n')
    if choice == 'y':
        start()
    elif choice == 'n':
        print('Hy i polllel na xyi')


def start():
    if i == 2:
        count = [0, 0]
    elif i == 3:
        count = [0, 0, 0]
    elif i == 4:
        count = [0, 0, 0, 0]

    deck = [2, 3, 4, 6, 7, 8, 9, 10, 11] * 4
    random.shuffle(deck)

    n = 0
    while n < i:
        print(f'{n} player walks')
        while True:
            choice = input('Take the card? y/n\n')
            if choice == 'y':
                current = deck.pop()
                print(f'You got a card: {current}')
                count[n] += current
                if count[n] > 21:
                    print(f'You have {count[n]} points\n You lose - Ebatb tb| /\ox')
                    break
                else:
                    print(f'You have {count[n]} points')
            elif choice == 'n':
                print(f'You have {count[n]} points')
                break
        n += 1
    result = 0
    winner = 0
    n = 0
    while n < i:
        if result < count[n] < 21:
            result = count[n]
            winner = n
        n += 1
    print(f'Player {winner} wins')
    game()


choice = input('Do you want to play? y/n\n')
if choice == 'y':
    choice = int(input('How many people will play?\nNumber of players from 2 to 4\n'))
    if choice == 2:
        i = 2
    elif choice == 3:
        i = 3
    elif choice == 4:
        i = 4
    start()
elif choice == 'n':
    print('Hy i polllel na xyi')

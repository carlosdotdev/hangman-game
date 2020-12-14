import os


def title():
    print('HANGMAN: THE GAME!')


def clear():
    return os.system('clear')


def pause():
    return input('Press any button to continue')


def execute():
    clear()

    title()

    secret_word = str(input('Type here the secret word: '))
    tip = ''
    current_found = ''
    hits = 0
    chances = 5

    add_or_not = input('Add tip (Y/N): ')

    if add_or_not == 'y' or add_or_not == 'Y' or add_or_not == 'YES' or add_or_not == 'yes' or add_or_not == 'Yes':
        tip = input('tip: ')

    clear()

    for word in secret_word:
        if word == ' ' or word == '-':
            current_found = current_found + ' '
        else:
            current_found = current_found + '-'

    if secret_word.__len__() != 0:

        while hits != secret_word.__len__() and chances > 0:
            left_letters = (secret_word.__len__() - hits -
                            secret_word.count(' ') - secret_word.count('-'))

            title()

            print(
                f'Secret word: {current_found} | Left: {left_letters} | Chances: {chances}')

            if chances <= 3 and tip.__len__() > 0:
                print(f'tip: {tip}')

            bet = str(input('Type here: '))
            num = -1

            clear()

            if bet == secret_word:
                hits = secret_word.__len__()
                break

            if bet.__len__() > 1:
                chances = 0
                break

            if current_found.count(bet) == 0:
                for word in secret_word:
                    num = num + 1

                    if word == bet:

                        new_list = list(current_found)
                        new_list[num] = word
                        current_found = ''
                        for index in new_list:
                            current_found = current_found + index
                        hits = hits + 1
            else:
                chances = chances - 1

            if not bool(secret_word.count(bet)):
                chances = chances - 1

        if hits == secret_word.__len__():
            clear()
            print('YOU WINS!!!')
            print(f'Secret Word: {secret_word}')

        elif chances == 0:
            clear()
            print('YOU LOSE')
    else:
        clear()
        print('Secret word is not found')
        pause()
        clear()
        execute()


execute()

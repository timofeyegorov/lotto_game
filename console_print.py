
def show_card(player_card, is_human):
    if is_human:
        print(f'{"-"*6} Ваша карточка {"-"*5}')
    else:
        print(f'{"-" * 3} Карта соперника {"-" * 3}')
    print(*player_card[:9])
    print(*player_card[9:18], sep=' ')
    print(*player_card[18:27], sep=' ')
    print('-'*26)

if __name__ == '__main__':
    show_card([i for i in range(27)], True)
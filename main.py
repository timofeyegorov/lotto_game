from game import Game
from player import Player
from console_print import show_card

game = Game()
print('Игра началась!!!')
player_1 = Player()
player_2 = Player(is_human = False)

while True:
    num, residue = game.step()
    print(f'Новый бочонок: {num} (осталось {residue})')
    show_card(player_1.card, player_1.is_human)
    show_card(player_2.card, player_2.is_human)
    choice = input('Зачеркнуть цифру? (y/n): ')
    num = game.transform_num(num)
    if choice == 'y':
        if num in player_1.card:
            player_1.drop_number(num)
        else:
            print('Такого числа нет на Вашей карте - Вы проиграли!!!')
            break
    if choice == 'n':
        if num in player_1.card:
            print('Такое число есть нв Вашей карте - Вы проиграли!!!')
            break
    player_2.drop_number(num)
    if residue < 77:
        check_player_1 = player_1.check_win()
        check_player_2 = player_2.check_win()
        if (check_player_1 == True) & (check_player_2 == True):
            print('Ничья!')
            break
        elif (check_player_1 == True) & (check_player_2 == False):
            print('Ура! Вы победили!!!')
            break
        elif (check_player_1 == False) & (check_player_2 == True):
            print('Вы проиграли :(')
            break






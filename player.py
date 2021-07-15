import numpy as np
import random

class Player:

    def __init__(self, is_human = True):
        cells = [str(i) for i in range(1, 91)]
        choice = random.sample(cells, 15)
        choice.sort()
        sampling_row_1 = choice[:5] + [' ' for i in range(4)]
        sampling_row_2 = choice[5:10] + [' ' for i in range(4)]
        sampling_row_3 = choice[10:15] + [' ' for i in range(4)]
        self.is_human = is_human
        self.card = []
        for i in range(3):
            for j in range(9):
                if i == 0:
                    self.card.append(np.random.choice(sampling_row_1))
                    sampling_row_1.pop(sampling_row_1.index(self.card[-1]))
                if i == 1:
                    self.card.append(np.random.choice(sampling_row_2))
                    sampling_row_2.pop(sampling_row_2.index(self.card[-1]))
                if i == 2:
                    self.card.append(np.random.choice(sampling_row_3))
                    sampling_row_3.pop(sampling_row_3.index(self.card[-1]))
        for i in range(len(self.card)):
            if len(self.card[i]) == 1:
                self.card[i] = ' ' + self.card[i]

    def drop_number(self, number):
        try:
            self.card[self.card.index(number)] = ' -'
        except ValueError:
            pass

    def check_win(self):
        check_result = len(np.unique(self.card)) == 2
        return check_result


if __name__ == '__main__':
    game = Player()
    print(game.card)
    print(game.card[1])
    game.drop_number(game.card[1])
    print(game.card)
    print(game.check_win())
    print(len(np.unique([' ',' -'])))




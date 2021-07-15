import numpy as np

class Game:

    def __init__(self):
        self.keg = [i for i in range(1, 91)]

    def step(self):
        choice = np.random.choice(self.keg)
        self.keg.pop(self.keg.index(choice))
        return choice, len(self.keg)

    def transform_num(self, number):
        number = str(number)
        if len(number) == 1:
            number = ' ' + number
        return number

if __name__ == '__main__':
    keg = [i for i in range(1, 91)]
    while True:
        choice = int(input(''))
        keg.pop(choice - 1)
        print(keg)
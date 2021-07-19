from game import Game
from player import Player

class TestGame:

    def test_init(self):
        game = Game()
        assert len(game.keg) == 90

    def test_step(self):
        game = Game()
        game.step()
        assert game.step()[0] in [i for i in range(1, 91)]
        assert len(game.keg) == 88

    def test_transform_num(self):
        game = Game()
        result = game.transform_num(1)
        assert len(result) == 2

class TestPlayer:

    def test_init(self):
        player = Player()
        assert len(player.card) == 27

    def test_drop_number(self):
        player = Player()
        drop = player.drop_number(player.card[0])
        assert player.card[player.card.index(player.card[0])] == ' -'

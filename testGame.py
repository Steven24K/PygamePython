class TestGame:
    def __init__(self, game):
        self.Game = game
    def test_run(self):
        self.Game.run()

     

from game1 import MainMenu

testObject = TestGame(MainMenu("Test Game", 1200, 600))
testObject.test_run()


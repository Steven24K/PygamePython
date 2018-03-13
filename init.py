from game1 import MainMenu
from game2 import MainGame
from game3 import Game3
from game4 import Game4
from game5 import Game5
from game6 import Game6

import que

#Create a new game and run the program
#Entry point for the application, from here you start the first level, in this case the main menu
game_height = 600
game_width = 1200

#Create a new Queue of games
games = que.List()


#We insert all games in the Que, first in first out
games.Enqueue(MainMenu("Main Menu", game_width, game_height))
games.Enqueue(MainGame("Game 1", game_width, game_height))
games.Enqueue(Game3("Game 3", game_width, game_height))
games.Enqueue(Game4("Game 4", game_width, game_height))
games.Enqueue(Game5("Game 5", game_width, game_height))
games.Enqueue(Game6("Game 6", game_width, game_height))


if __name__ == "__main__":
    #After the insertions, we itterate over the que and executie each game until the que is empty
    while not games.IsEmpty():
        games.Dequeue().run()

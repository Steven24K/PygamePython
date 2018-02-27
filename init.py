from game1 import MainMenu
from game2 import MainGame
from game3 import Game3
from game4 import Game4
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
#Todo: Add Game 3 and 4 to the Que


if __name__ == "__main__":
    #After the insertions, we itterate over the que and executie each game until the que is empty
    while not games.IsEmpty():
        games.Dequeue().run()

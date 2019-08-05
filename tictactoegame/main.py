import sys 
sys.path.append("./tictactoe")
from tictactoe.game import Game


total_games=int(input("Please select number of games in this series:"))
print("OK! This series will consist of {} games.".format(total_games))
game=Game(total_games)
game.play()

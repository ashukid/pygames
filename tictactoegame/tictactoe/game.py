from board import Board
from player import Player

class Game:

    def __init__(self,total_games):

        self.total_games=total_games
        self.init_board()
        self.player1=Player(1,"x")
        self.player2=Player(2,"0")


    def init_board(self):
        self.board=Board()
        # self.board.show_board()

    def select_position(self,player_number):

        print("Player {}: Which square do you choose ?".format(player_number))
        next_position=list(map(int,input().split()))
        # check valid position
        return next_position

    def check_valid(self,position):
        x=position[0]-1
        y=position[1]-1

        # bound condition
        if(x<0 or x>3 or y<0 or y>3):
            return 0

        # valid condition
        if(self.board.board[x][y]!=" "):
            return 0
        return 1


    def play(self):

        current_player=self.player1
        number_of_times_played=0
        player1_win=0
        player2_win=0
        total_games_played=0

        while(True):

            next_position=self.select_position(current_player.player_number)

            while(not self.check_valid(next_position)):
                print("Invalid Position. Please select again")
                next_position=self.select_position(current_player.player_number) 
            
            self.board.update_board(next_position,current_player.player_symbol)

            self.board.show_board()
            game_status,win_symbol=self.board.check_status()
            if(game_status):
                if(win_symbol==self.player1.player_symbol):
                    print("Congratulations Player1")
                    player1_win+=1
                else:
                    print("Congratulations Player2")
                    player2_win+=1

                total_games_played+=1
                if(total_games_played==self.total_games):
                    self.end_game(player1_win,player2_win)
                    break
                print("\nStarting game {} of {}\n".format(total_games_played+1,self.total_games))
                self.init_board()
                self.current_player=self.player1
                continue

            if(number_of_times_played==9):
                print("Game Drawn")
                total_games_played+=1
                if(total_games_played==self.total_games):
                    self.end_game(player1_win,player2_win)
                    break

                print("\n Starting game {} of {}\n".format(total_games_played+1,self.total_games))
                self.init_board()
                self.current_player=self.player1
                continue

            current_player=self.change_player(current_player)
            number_of_times_played+=1


    def end_game(self,player1_win,player2_win):
        if(player1_win>player2_win):
            print("Congrats Player1. You have won the series!")
        elif(player2_win>player1_win):
            print("Congrats Player2. You have won the series!")
        else:
            print("Series Drawn")

    def change_player(self,player):
        if(player.player_number==1):
            return self.player2
            
        return self.player1

if(__name__=="__main__"):
    game=Game()
    game.play()

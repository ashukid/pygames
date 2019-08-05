class Board:

    def __init__(self): # later will pass n
        
        # intialize board with all zeros
        self.board=[[" " for _ in range(3)] for _ in range(3)]


    def show_board(self):
        
        for row in range(3):
            print(self.board[row][0],end="")
            print("|",end="")
            print(self.board[row][1],end="")
            print("|",end="")
            print(self.board[row][2])
            
            if(row!=2):
                print("------")

    def check_status(self):

        status,symbol=self.check_rows()
        if(status):
            return status,symbol

        status,symbol=self.check_columns()
        if(status):
            return status,symbol

        status,symbol=self.check_diagonals()
        if(status):
            return status,symbol

        return 0,None

        
    def check_rows(self):

        for row in range(3):
            current_row=self.board[row]
            symbol=current_row[0]
            if(symbol==" "):
                return 0,None
            if(current_row[1]==symbol and current_row[2]==symbol):
                return 1,symbol
        return 0,None


    def check_columns(self):

        for column in range(3):
            symbol=self.board[0][column]
            if(symbol==" "):
                return 0,None
            if(self.board[1][column]==symbol and self.board[2][column]==symbol):
                return 1,symbol
        return 0,None


    def check_diagonals(self):
        
        #take the middle element
        symbol=self.board[1][1]
        if(symbol==" "):
            return 0,None
        # clockwise diagonal
        if(self.board[0][0]==symbol and self.board[2][2]==symbol):
            return 1,symbol

        #anticlockwise diagonal
        if(self.board[0][2]==symbol and self.board[2][0]==symbol):
            return 1,symbol

        return 0,None


    def update_board(self,position,symbol):
        
        x=position[0]-1
        y=position[1]-1
        self.board[x][y]=symbol


        
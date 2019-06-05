class Hangman:

    def __init__(self):
       
        self.sc=20 #space count
        self.line1=" "*self.sc + " +---+"
        self.line2=" "*self.sc + "     |"
        self.line3=" "*self.sc + "     |"
        self.line4=" "*self.sc + "     |"
        self.line5=" "*self.sc + "     |"
        self.line6=" "*self.sc + "======" 
        self.count=-1

    def draw(self):
        print(self.line1)
        print(self.line2)
        print(self.line3)
        print(self.line4)
        print(self.line5)
        print(self.line6)
    
    def add_head(self):
        self.line2=" "*self.sc + " o   |"
    
    def add_body(self):
        self.line3=" "*self.sc + "/|\  |"

    def add_legs(self):
        self.line4=" "*self.sc + "/ \  |"

    def hang(self):
        self.line5=" "*self.sc + "hanged"
   
    def hang_and_draw(self):
        self.count+=1
        if(self.count==0):
            self.add_head()
            self.draw()
            return False
        if(self.count==1):
            self.add_body()
            self.draw()
            return False
        if(self.count==2):
            self.add_legs()
            self.draw()
            return False
        if(self.count==3):
            self.hang()
            self.draw()
            return True


if(__name__=='__main__'):
    man=Hangman()
    man.hang_and_draw()
    man.hang_and_draw()
    man.hang_and_draw()
    man.hang_and_draw()
    man.hang_and_draw()
    man.hang_and_draw()

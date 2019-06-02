class Hangman:

    def __init__(self):
       
        self.sc=20 #space count
        self.line1=" "*self.sc + " +---+"
        self.line2=" "*self.sc + "     |"
        self.line3=" "*self.sc + "     |"
        self.line4=" "*self.sc + "     |"
        self.line5=" "*self.sc + "     |"
        self.line6=" "*self.sc + "======" 

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
    
if(__name__=='__main__'):
    man=Hangman()
    man.draw()
    man.add_head()
    man.draw()
    man.add_body()
    man.draw()
    man.add_legs()
    man.draw()
    man.hang()
    man.draw()

import random
import time
from hangman import Hangman

def wordPicker():
    wordset=["cat","rat","bat",
            "father","mother","sister","brother"]
    idx=random.randrange(0,len(wordset))
    return wordset[idx]

def printBreak():
    print("\n"+ "-"*10 + "#"*20 + "-"*10 + "\n")

def playGame():
   
    # picking word
    print("Picking a word...")
    time.sleep(2)
    word=wordPicker()
    wordlen=len(word) 
    print("Word picked !! Total :{} letters".format(wordlen))
    printBreak()

    # initializing hangman
    man=Hangman()
  
    # main game loop
    guessed_words=["_"]*wordlen 
    while True:
        ch=input("Guess a number : ")
        flag=0
        for i in range(wordlen):
            if(word[i]==ch and guessed_words[i]=="_"):
                guessed_words[i]=ch
                flag=1
                break

        if(flag):
            print("Right Guess !!")
            man.draw()
        else:
            print("Wrong Guess !!")
            dead=man.hang_and_draw()
            if(dead):
                printBreak()
                break
        print(" ".join(guessed_words))
        print("\n")

        if(guessed_words.count("_")==0):
            print("Congrats! YOU WON !!")
            printBreak()
            break

playGame()

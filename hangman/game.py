import random
import time
from draw import Hangman

def pickWord():
    wordset=["cat","rat","bat",
            "father","mother","sister","brother"]
    idx=random.randrange(0,len(wordset))
    return wordset[idx]

def printBreak():
    print("\n"+ "-"*10 + "#"*20 + "-"*10 + "\n")

print("Picking a word...")
time.sleep(2)
word=pickWord()
wordlen=len(word)
print("Word picked !! It contains : {} letters".format(wordlen))
printBreak()


guessed_words=[-1]*wordlen 
while True:
    ch=input("Guess a number : ")
    

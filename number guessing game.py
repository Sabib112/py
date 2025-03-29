import random
import time


number=random.randint(1, 100)

def intro():
    print("may i ask your name?")
    global name
    name=input()
    print(name,", welcome to number guessing game, i am thinking of a number between 1 and 100")

    if (number %2== 0):
        x = "even"
    else:
        x= "odd"

    print(f"\this is a {x} number")
    time.sleep(.5)
    print('go ahead and guess the number')

def pick():
    guessTaken = 0
    while guessTaken < 6:
        time.sleep(.5)
        enter=(input("guess the number: "))  
        try:
            guess = int(enter) 
            if guess<=100 and guess>=1:
                 guessTaken += 1
                 if guessTaken <6:
                    if guess < number:
                         print("your guess is too low")
                    if guess>number:
                         print("your guess is too high")
                
                    if guess!=number:
                        print("try again")
                    if guess==number:
                        break
            else:
                print("please enter a number between 1 and 100")
        except :
            print("i dont think this is a number")


    if guess==number:
        print("you guessed it!")
        print(f"it took you {guessTaken} tries")
    if guess!=number:
        print("try again, you have", 6-guessTaken, "tries left")
playAgain='yes'
while playAgain=='yes' or playAgain=='y':
    intro()
    pick()
    print("do you want to play again?")
    playAgain=input()
   
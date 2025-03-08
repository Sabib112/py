import random
playing = True
randomNumber=random.randint(10,20)
print("guess the number between 10 and 20")

while playing:
    guess=int(input("Enter your guess:"))
    if guess==randomNumber:
        print("you won!")
        print("the number is",randomNumber)
    
    else:
        print("you lost!")
        print("try again!")
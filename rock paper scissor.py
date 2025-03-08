import random

options = ['rock', 'paper', 'scissor']
userChoice= input("rock, paper or scissor? ")
computerChoice = random.choice(options)

print("your choice: ", userChoice)
print("computer choice: ", computerChoice)

if userChoice == computerChoice:
    print("It's a tie!")
    
elif userChoice=='rock' and computerChoice=='scissors':
    print("You win!")

elif userChoice=='paper' and computerChoice=='rock':
    print("You win!")

elif userChoice=='scissors' and computerChoice=='paper':
    print("You win!")

else:
    print("You lose!")
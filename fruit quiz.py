import random

class FruitQuiz:
    def __init__(self):
        self.fruits = {"apple": "red",
                       "banana": "yellow",
                       "orange": "orange",
                       "grape": "purple",}
        
    def quiz(self):
        while True:
            fruit,color=random.choice(list(self.fruits.items()))
            print(f"What color is a {fruit}?")
            answer=input()

            if(answer.lower() == color):
                print("Correct!")
       
            else:
                print(f"Wrong! The correct answer is {color}.")
            
            option = int(input("Do you want to continue? (1 for yes/ 0 for no): "))
            if option == 1:
                continue
            else:
                break

print("Welcome to the fruit quiz app")
fq=FruitQuiz()
fq.quiz()
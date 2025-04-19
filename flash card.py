class Flashcard:
    def __init__ (self,word,meaning):
        self.word = word
        self.meaning = meaning

    def __str__(self):
        return self.word + " ( " + self.meaning +" ) "
    
flash=[]
print("Welcome to the flashcard app")

while True:
    word= input("Enter the word: ")
    meaning= input("Enter the meaning: ")

    flash.append(Flashcard(word,meaning))
    option= int(input("Do you want to add more flashcards? (1 for yes, 0 for no): "))

    if option == 1:
        continue
    else:
        break

for i in flash:
    print(">",i)
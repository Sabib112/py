word=input("enter a word: ")

item=input("enter the alphabet you want to search: ")

found=False
for i in word:
    if i==item:
        found=True
        break
if found==True:
    print(f"{item} is found in the word")
else:
    print(f"{item} is not found in the word")
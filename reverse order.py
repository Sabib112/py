word = input("enter a word: ")
reversed=''
for i in word:
    reversed= i + reversed
print("original word: ",word)
print("reversed word: ",reversed)
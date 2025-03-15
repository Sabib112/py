def word_matching(words):
    count=0
    lst=[]

    for word in words:
        if len(word)>1 and word[0]== word[-1]:
            count+=1
            lst.append(word)
    
    print("list of woeds with same first and last characters are : ",lst)
    return count

count=word_matching(["abc",'aba',"aia","asd"])
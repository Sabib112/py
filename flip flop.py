def flip_flop(tup):
    start=0
    end=len(tup)-1

    while start<end:
        if (tup[start] != tup[end]):
            return False
        start +=1
        end-=1
    return True

tup=(1,2,3,3,2,1)
if flip_flop(tup):
    print("The tuple is flip flop")
else:
    print("The tuple is not flip flop")
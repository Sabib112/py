weather= (1,0,0,1,1,0,1)
sunny=0
rainy=0
for i in range(len(weather)):
    if weather[i]==0:
        rainy+=1
    else:
        sunny+=1
if sunny>rainy:
    print("Sunny")
else: 
    print("Rainy")
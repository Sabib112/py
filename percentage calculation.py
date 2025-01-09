print("Enter your marks that you obtained in each subject")

math= int(input("Math: "))

science= int(input("Science: "))

bgs= int(input("BGS: "))

agriculture= int(input("Agriculture: "))

ict= int(input("ICT: "))

#sum of all marks
sum= math+science+bgs+agriculture+ict

percentage= (sum/500)*100

print("The percentage is: ",percentage,"%")
amount = int(input("Enter the amount : "))

note1 = amount // 500
print("Note 500 : ",note1)

note2 = (amount % 500)//200
print("Note 200 : ",note2)

note3 = ((amount % 500)%200)//100
print("Note 100 : ",note3)

note4 = (((amount % 500)%200)%100)//20
print("Note 20 : ",note4)

note5 = ((((amount % 500)%200)%100)%20)//10
print("Note 10 : ",note5)
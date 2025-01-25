medical_cause = input("Do you have a medical cause? y/n? ")


if medical_cause=="y":
    print("you are eligible for exam")

else:
    attendence= int(input ("enter the number of class attended "))
    if attendence>75 :
        
        marks= int(input("enter your marks"))
    
        if marks>50:
            print("you are eligible for exam")

        else:
            print("you are not eligible for exam")

    else:
        print("you are not eligible for exam")
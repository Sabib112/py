import time

def shutdown():
    print("Checking conditions before shutting down...")
    
    condition_1 = True  
    condition_2 = True 


    if condition_1 and condition_2:
        user_input = input("Do you want to shut down the program? (yes/no): ").lower()

        if user_input == 'yes':
            print("Shutting down...")
            time.sleep(2)  
            print("Program is now closed.")
        elif user_input == 'no':
            print("Sorry, the program will not shut down.")
        else:
            print("Invalid input. Please type 'yes' or 'no'.")
    else:
        print("Conditions not met. Cannot shut down.")


shutdown()
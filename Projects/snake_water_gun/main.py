""" Snake Water Gun Game """
   
import random

computer=random.choice(["S","W","G"])
you=input("Enter Your Choice ( S for snake , W for water , G for gun) : ").upper()



print("Computer's Choice is :",computer)

if computer==you:
    print("Tie")

else:
    if computer=="S" and you=="W":
        print("You Lose!")
    elif computer=="S" and you=="G":
        print("You Win!")
    elif computer=="W" and you=="S":
        print("You Win!")
    elif computer== "W" and you=="G":
        print("You Lose!")
    elif computer == "G" and you=="S":
        print("You Lose!")
    elif computer == "G" and you== "W":
        print("You Win!")

    else: print("Invalid Choice")




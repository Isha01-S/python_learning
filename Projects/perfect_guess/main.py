'''We are going to write a program that generates a random number and asks the user to
guess it.
If the player’s guess is higher than the actual number, the program displays “Lower
number please”. Similarly, if the user’s guess is too low, the program prints “higher
number please” When the user guesses the correct number, the program displays the
number of guesses the player used to arrive at the number.
Hint: Use the random module'''
'''You have 5 lives'''

import random

n = random.randint(1,21) #generates random number
lives = 5 #you have only 5 lives
a = -1 
guesses = 0
print("Welcome to the Perfect Guess!!")

while (1):
    print(f"lives left : {lives-guesses}") #finds out lives left
    guesses += 1 #increasees the guess by 1
    
    a = int(input("Guess a number (from 1 to 20): ")) #takes number from the user
    if a==n: #checks if the user has guessed the right number
        print("You won!!")
        break
    if guesses==lives: # checks if all lives are used
        print("Game Over!!!!")
        break
    
    if a < n:
        print("!Enter a larger number!")

    if a > n: 
        print("!Enter a smaller number!")
    
    #prints all the information life correct number, guessed number, number of guesses
print(f"The correct number is : {n}")
print(f"Your guess is : {a}")
print(f"The number of guesses are : {guesses}")


    

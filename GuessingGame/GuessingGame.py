print("Guess the number!")
import random
n = random.randint(1, 99)
guess = int(input("Enter an interger from 1 to 99:   "))
while True:
     if guess < n:
         print("Guess is too low!")
         guess = int(input("Enter an interger from 1 to 99:   "))
     elif guess > n:
         print("Guess is too high!")
         guess = int(input("Enter an interger from 1 to 99:   "))
     else:
         print("You guessed it right!")
         break
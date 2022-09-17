import random

number= random.randint(1,10)
attempt= 1
guess = int(input("Guess the number : "))

while(True):
    if(guess>number):
        guess=int(input("Guess another number.This noe is too big:"))
        attempt+=1
    elif(guess<number):
        guess=int(input("Guess another number.This noe is too less:"))
        attempt+=1
    else:
        print(f"Thats the number! You guessed it right in {attempt} attempts")
        break
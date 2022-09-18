'''perfect guessing game'''

import random

number = random.randint(1,10)
attempt=1


guess= int(input("Enter the right number :"))

while(True):
    if guess>number:
        guess=int(input("Enter again, the number is too big:"))
        attempt+=1
    elif guess<number:
        guess=int(input("Enter again, the number is too less:"))
        attempt+=1
    else:
        print(f"Thats the the number!!! you guessed right number in {attempt} attempts")
        break

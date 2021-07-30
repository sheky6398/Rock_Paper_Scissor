import random

a=int(input('Enter First Number: '))
b=int(input('Enter second Number'))
attempt=0
Number=range(a,b)
Answer=random.randint(a,b)

while True:
    attempt+=1   
    Guess=int(input('Enter the Guess Number: '))
    if Answer>Guess:
        print(f"You Guessed the number {Guess} that is too Small")
    elif Answer<Guess:
        print(f"You Guessed the number {Guess} that is too High")
    else:
        print(f'You Guessed the number in {attempt} attempts')
        break
print("Thanks for playing the game")
        
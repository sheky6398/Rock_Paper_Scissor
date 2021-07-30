import random as rd

print("LET'S PLAY ROCK , PAPER and SCISSORS GAME:".center(70,"*"))
more='yes'
while True and more=='yes':
    
    print("\nPlease enter your choice\n")
    player=input("rock (r), paper (p) or scissors (s)?")


    if player=='r' or player=='p' or player=='s':
        print(player,'VS',end=' ')
        
        computer=rd.choice(['r','s','p'])
        
        if computer=='r':
            print("O")
        elif computer=='s':
            print('__')
        else:
            print(">8")
    
        if computer==player:
            print("DRAW")
        
        elif player=='r' and computer=='s':
            print("Player wins!")
        elif player=='r' and computer=='p':
            print('Computer wins!')
        
        elif player=='p' and computer=='r':
            print("Player wins!")
        elif player=='p' and computer=='p':
            print('Computer wins!')
            
        while True:
            more=input("WANNA PLAY MORE--> ENTER 'yes' OR 'no' ".center(50,"*"))
            if more=='yes':
                break
            elif more=='no':
                break
            
            else:
                print("PLEASE ENTER EITHER 'yes' OR 'no':")


    else:
        print("PLEASE ENTER THE VALID CHARACTER")
print("THANK YOU FOR PLAYING".center(70,'-'))
                                            #THE PERFECT GUESS
# We are going to write a program that genarates a random number and asks the user to guess it.

"""If the player guess is higher than the actual number, the program display LOWER NUMBER PLACE.
similarly if the user's guess is too low, the program prints HIGHER NUMBER PLEASE
when the user gusses the correct number, the program displays the number of guess the player
used to arrive at the manner"""
import random
randNumber=random.randint(1,100)
# print(randNumber)
userGuess=None
gusses=0

while(userGuess !=randNumber):
        
    userGuess=int(input("Enter A Number For Guess: "))
    gusses+=1

    if userGuess==randNumber:
        print("Your Guess Number Is Right...")
    else:
        if (userGuess>randNumber):
            print("Your Guess Number Is Wrong! Enter A Smaller Number..")
        else:   
             print("Your Guess Number Is Wrong! Enter A Larger Number..")

print(f'Your Total Guess Number Is {gusses}.')
with open("project2/highscore.txt",'r')as f:
    highcsore=int(f.read())

if(gusses<highcsore):
    print("You have just broken the high score!")
    with open("highscore.txt","w") as f:
        f.write(str(gusses))
        






















# Stone Paper siccor
import random

def stonePaperSiccor():
    inp = int(input("Enter 1(for stone), 2(for paper), 3(scissor): \n"))
    a = random.randint(1,3)
    if a==1:
        comp = "Stone"
    elif a==2:
        comp = "Paper"
    else:
        comp = "Scissor"

    print("computer choose", comp)
    
    if inp == 1 and comp == "Stone":
        return("Computer wins!!")
    elif inp == 1 and comp == "Scissor":
        return("You win!!")
    elif inp == 2 and comp == "Stone":
        return("You win!!")
    elif inp == 2 and comp == "Scissor":
        return("Computer wins!!")
    elif inp == 3 and comp == "Stone":
        return("Computer wins!!")
    elif inp == 3 and comp == "Paper":
        return("You win!!")
    else:
        return("Game tie!!")

print(stonePaperSiccor())

# solution 2

import random
lst=["rock", "paper", "Scissor"]
a=input("Enter yout choise: ").lower()
rno = random.choices(lst)
print(f'CPU choose {rno}')
print(f'you chosoe {a}')
if a==rno:
    print("Game tie")
elif (a==lst[1] and rno==lst[1]) or(a==lst[2] and rno==lst[1]) or(a==lst[0] and rno==lst[2]):
    print("You won!!")
else:
    print("CPU won!!")
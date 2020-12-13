import random 
turns=10
bscore= 0
ascore=0
while turns>0:
    a=int(input("Write 1 for stone, 2 for paper and 3 for scissor "))
    Comp= random.choices(["Stone","Paper","Scissor"])
    if a==1:
        if Comp==["Stone"]:
            print("draw")
        elif Comp==["Scissor"]:
            print("won")
            ascore=ascore+1  
        elif Comp==["Paper"]:
            print("lost")
            bscore=bscore+1  
    elif a==3:
        if Comp==["Stone"]:
            print("lost")
            bscore=bscore+1 
        elif Comp==["Scissor"]:
            print("draw") 
        elif Comp==["Paper"]:
            print("won")
            ascore=ascore+1   
    elif a==2:
        if Comp==["Stone"]:
            print("won")
            ascore=ascore+1  
        elif Comp==["Scissor"]:
            print("lost") 
            bscore=bscore+1 
        elif Comp==["Paper"]:
            print("draw")
    else:
        turns=turns+1 
        print("Please enter 1 or 2 or 3")
    turns=turns-1
    print("Turns left", turns)
# Result Logic
if ascore>bscore:
    print("You won as", ascore,">", bscore)
elif ascore<bscore:
    print("You lost as", ascore,"<", bscore)
else:
    print("Game drawed") 


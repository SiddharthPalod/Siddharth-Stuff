Hidden=15 
g=9 #guesses left 
while g>0:
    a=int(input("Enter your number "))
    if a>Hidden:
        print("Your number is greater")
    elif a<Hidden:
        print("Your number is lesser")
    elif a==Hidden:
        print("You won")
        break
    g= g-1
    print("Guesses left", g)
    if g==0:
        print("You Lost")
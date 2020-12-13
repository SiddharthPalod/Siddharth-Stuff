num1=int(input("Number 1 "))
num2=int(input("Number 2 "))
opt=input("Operator to use +-/* ")

if opt=="+":
    if num1=="59" and num2=="9" or num1 =="9" and num2=="59":
        print(77)
    else:
        print(num1+num2)   
elif opt=="*":
    if num1=="45" and num2=="3" or num1 =="3" and num2=="45":
        print(555)
    else:
        print(num1*num2)
elif opt=="/":
    if num1=="56" and num2=="6":
        print(4)
    else:
        print(num1/num2)
elif opt=="-":
        print(num1+num2)
else:
    opt=input("What operator to use +-/* ")   
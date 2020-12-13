def getdate():
    import datetime
    return datetime.datetime.now()
x=int(input("Press 1 to lock and 2 to retrive "))
a= int(input("Enter 1 for Rohan, 2 for Harry and 3 for Hamad "))

if x==1: 
    if a==1:
        b=int(input("Press 1 for diet and 2 for exercise "))
        if b==1:
            r1=open("r-diet.txt", "a")
            r1.write(input("Food "))
        elif b==2:
            r2=open("r-ex.txt", "w")
            r2.write(input("Exercise ")/n)
        else:
            b=int(input("Press 1 for diet and 2 for exercise "))
    elif a==2:
        b=int(input("Press 1 for diet and 2 for exercise "))
        if b==1:
            r1=open("h-diet.txt", "w")
            r1.write(input("Food ")/n)
        elif b==2:
            r2=open("h-ex.txt", "w")
            r2.write(input("Exercise ")/n)
        else:
            b=int(input("Press 1 for diet and 2 for exercise "))            
    elif a==3:
        b=int(input("Press 1 for diet and 2 for exercise "))
        if b==1:
            r1=open("ham-diet.txt", "w")
            r1.write(input("Food ")/n)
        elif b==2:
            r2=open("ham-ex.txt", "w")
            r2.write(input("Exercise ")/n)    
        else:
            b=int(input("Press 1 for diet and 2 for exercise "))
if x==2:
    if a==1:
        b=int(input("Press 1 for diet and 2 for exercise "))
        if b==1:
            r1=open("r-diet.txt", "r")
            for line in r1:
                print(getdate(), line)
        elif b==2:
            r2=open("r-ex.txt", "r")
            for line in r2:
                print(getdate(),line)
        else:
            b=int(input("Press 1 for diet and 2 for exercise "))
    elif a==2:
        b=int(input("Press 1 for diet and 2 for exercise "))
        if b==1:
            r1=open("h-diet.txt", "r")
            for line in r1:
                print(getdate(),line)
        elif b==2:
            r2=open("h-ex.txt", "r")
            for line in r2:
                print(getdate(),line)
        else:
            b=int(input("Press 1 for diet and 2 for exercise "))      
    elif a==3:
        b=int(input("Press 1 for diet and 2 for exercise "))
        if b==1:
            r1=open("ham-diet.txt", "r")
            for line in r1:
                print(getdate(),line)
        elif b==2:
            r2=open("ham-ex.txt", "r")
            for line in r2:
                print(getdate(),line)
        else:
            b=int(input("Press 1 for diet and 2 for exercise "))  
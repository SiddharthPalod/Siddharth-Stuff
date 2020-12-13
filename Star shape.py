n=int(input("How many lines: "))
a=int(input("1 or 0: "))
m=n-n+1

while n>=0 and a==0:
    print("*"*n)
    n=n-1 
while n>=m>0 and a==1:
    print("*"*m)
    m=m+1

    
 
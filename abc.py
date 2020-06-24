from math import *

def pr(n):
    x=0
    y=0
    for i in range(2,int(sqrt(n)+1)):
        if n%i==0:
            while(n%i==0):
                n//=i
                if i%2:
                    y+=1
                else:
                    x+=1
    if n>1 and n%2:
        y+=1
    return x,y

   
t=int(input())
while t:
    t=t-1
    n=int(input())
    p="Ashishgup"
    q="FastestFinger"
    if n==1:
        print(q)
    elif n==2:
        print(p)
    elif n%2:
        print(p)
    else:
        x,y=pr(n)
        if (x==1 and y==1) or y==0:
            print(q)
        else:
            print(p)
            
            
        
        
    
        
    
        

n = int(input())

while n>0:
    print(int(n),end=" ")
    if n==1:
        break
    elif n%2==0:
        n=n/2
        
    elif n%2==1:
        n=(n*3)+1


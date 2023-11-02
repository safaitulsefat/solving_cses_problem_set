
n = int(input())
for i in range(n):
    x,y=[int(x) for x in input().split()]
    if x==1 and y==1:
        print(1)
    elif x>=y:
        if x%2==0:
            print((x*x)-(y-1))
        else:
            r = (x-1)
            print(((r*r)+1)+(y-1))
    else:
        if y%2==0:
            r = (y-1)
            print(((r*r)+1)+(x-1))
        else:
           print((y*y)-(x-1))

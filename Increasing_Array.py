n = int(input())

x = list(map(int,input().split()))
count=0
for i in range(n):
    if i==n-1:
        break
    elif x[i]>x[i+1]:
        s=(x[i]-x[i+1])
        x[i+1]=x[i+1]+s
        count+=s

print(count)
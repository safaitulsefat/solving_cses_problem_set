n = int(input())
s=0
set_a = set()
set_b = set()
for i in range(1,n+1):
    s+=i
    
if s%2==0:
    half = s/2
    print("YES")
    for i in range(n,0,-1):
        if half>=i:
         set_a.add(i)
         half-=i
        else:
           set_b.add(i)
    print(len(set_a))
    print(*set_a)
    print(len(set_b))
    print(*set_b)
else:
    print("NO")
s = input()
ans=1
count=1
for i in range(len(s)):
    if i==len(s)-1:
        break
    elif s[i]==s[i+1]:
        count+=1
        if ans<count:
            ans=count
    else:
        count=1

print(ans)
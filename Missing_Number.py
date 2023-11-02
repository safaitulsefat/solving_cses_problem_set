'''
#in this problem i solve first then many test cases output  The time limit might be exceeding for your code because it has a nested loop structure, which can result in poor performance for larger input sizes. In your code, you have two nested loops. 
The outer loop runs from 1 to n, and the inner loop runs from 0 to n-2. This results in a time complexity of O(n^2).
If the value of n is large, this code can take a significant amount of time to run. In competitive programming or when dealing with larger inputs, it's essential to optimize your code to run efficiently within the given time limits.

n = int(input())
x=list(map(int,input().split()))

for i in range(1,n+1):
    for j in range(n-1):
        if i==x[j]:
            break
    
    if i!=x[j]:
        print(i)
        
'''


n = int(input())

x=set(map(int,input().split()))

for i in range(1,n+1):
    if i not in x:
        print(i)
    

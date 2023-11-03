n = int(input())

for i in range(1,n+1):
    total_two_knight = ((i*i)*((i*i)-1))/2
    atcking_chesse = 4*(i-2)*(i-1)
    
    result = total_two_knight - atcking_chesse
    print(int(result))
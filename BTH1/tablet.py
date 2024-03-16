import math

n = int(input())
count = 0 
limit = int((n /math.sqrt(2))) + 1

for i in range(3, limit):
    temp = math.sqrt(n * n - i * i)
    if temp*temp == int(temp)*int(temp):
        count += 1 

print(count)
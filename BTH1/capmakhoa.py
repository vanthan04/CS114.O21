import sys
from math import sqrt, gcd
L, R = map(int, sys.stdin.readline().split())

# https://gemini.google.com/app/258a368553801bc9
def arrsnt(n):
  primes = [True] * (n + 1)
  primes[0] = primes[1] = False
  for i in range(2, int(sqrt(n)) + 1):
    if primes[i]:
      for j in range(i * i, n + 1, i):
        primes[j] = False
  return [i for i in range(2, n + 1) if primes[i]]

arr =[]
arr = arrsnt(int(sqrt(10**10)+1000))

def checksdb(n):
  i = 0
  while arr[i] * arr[i] <= n: 
    while n % arr[i]==0:
      n //= arr[i]
      if n%arr[i]==0:
        return False
    i+=1
  return True

arrsdb = []
for i in range(L, R+1):
  if checksdb(i):
    arrsdb.append(i)

count=0

for i in range(len(arrsdb)):
    for j in range(i+1, len(arrsdb)):
        if gcd(arrsdb[i],arrsdb[j]) == 1:
          count+=1
print(count)
import sys
n=int(sys.stdin.readline())

points=[]
vectors=[]

for _ in range(n):
  line = sys.stdin.readline()
  line = line.replace('‐', '-')
  x,y = map(int,line.split())
  points.append([x,y])

def checkvuonggoc(arr1, arr2):
  return arr1[0]*arr2[0]+arr1[1]*arr2[1]==0

for i in range(n-1):
  x=points[i+1][0]-points[i][0]
  y=points[i+1][1]-points[i][1]
  vectors.append([x,y])

count=0

for i in range(len(vectors)-1):
  if checkvuonggoc(vectors[i], vectors[i+1]):
    if vectors[i]==[1,0]:
      if points[i+2][1]==points[i+1][1]-1:
        count+=1
    elif vectors[i]==[-1,0]:
      if points[i+2][1]==points[i+1][1]+1:
        count+=1
    elif vectors[i]==[0,1]:
      if points[i+2][0]==points[i+1][0]+1:
        count+=1
    else:
      if points[i+2][0]==points[i+1][0]-1:
        count+=1
  
print(count)

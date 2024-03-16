A = input().split()
xA = int(A[0])
yA = int(A[1])

B = input().split()
xB = int(B[0])
yB = int(B[1])

xAB = xA-xB
yAB = yA-yB

distance = ((xAB)**2+(yAB)**2)**0.5

# Tìm vector BC vuông góc với vector AB
xBC = -yAB
yBC = xAB

xC1 = xB + xBC
yC1 = yB + yBC

xC2 = xB - xBC
yC2 = yB - yBC

#Tìm vector AD vuông góc với vector AB
xAD = -yAB
yAD = xAB

xD1 = xA + xAD
yD1 = yA + yAD

xD2 = xA - xAD
yD2 = yA - yAD

print(f'({xA}, {yA}) ({xD2}, {yD2}) ({xC2}, {yC2}) ({xB}, {yB})')
print(f'({xA}, {yA}) ({xB}, {yB}) ({xC1}, {yC1}) ({xD1}, {yD1})')

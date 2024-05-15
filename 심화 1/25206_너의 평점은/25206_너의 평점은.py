import sys

sys.stdin = open("25206_너의 평점은.txt")

rank = {'A+':4.5, 'A0':4.0,'B+':3.5,'B0':3.0,'C+':2.5,'C0':2.0,'D+':1.5,'D0':1.0,'F':0}
total=0
sum=0

for i in range(20):
    I,S,R = input().split()
    if R == "P":
        continue
    total += float(S)
    sum += 1
print(total/sum)
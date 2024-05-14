import sys

sys.stdin = open("25206_너의 평점은.txt")

rank = ['A+','A0','B+','B0','C+','C0','D+','D0','F']
score = [4.5,4.0,3.5,3.0,2.5,2.0,1.5,1.0,0]
total=0
sum=0

for i in range(20):
    I,S,R = input().split()
    if R == "P":
        continue
    total += float(S)
    sum += 1
print(total/sum)
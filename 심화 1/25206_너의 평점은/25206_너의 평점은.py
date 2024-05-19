import sys

sys.stdin = open("25206_너의 평점은.txt")

rank = {'A+':4.5, 'A0':4.0,'B+':3.5,'B0':3.0,'C+':2.5,'C0':2.0,'D+':1.5,'D0':1.0,'F':0}
total=0
sum=0

for i in range(20):
    I,S,R = input().split() #각 과목 학점 등급으로 나누기
    if R == "P": # 등급이 P일 경우
        continue # 넘기기
    total += float(S) * rank[R] # 학점 * 랭크점수 더하기
    sum += float(S) # 학점 더하기
print(total/sum)

rank = {'A+':4.5, 'A0':4.0,'B+':3.5,'B0':3.0,'C+':2.5,'C0':2.0,'D+':1.5,'D0':1.0,'F':0}
total=0
sum=0

for i in range(20):
    I,S,R = input().split() #각 과목 학점 등급으로 나누기
    if R == "P": # 등급이 P일 경우
        continue # 넘기기
    total += float(S) * rank[R] # 학점 * 랭크점수 더하기
    sum += float(S) # 학점 더하기
print(total/sum)
import sys

sys.stdin = open("5622_다이얼.txt")

dial=["ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"] #다이얼번호 배열
S = input() #문자열 가져오기
dial_sum=0; #숫자합
for i in range(len(S)): #문자갯수만큼 반복 WA:2
    for j in dial: # 배열만큼 반복
        if S[i] in j: #문자 마다 배열에 맞는 인덱스값 가져오기
            dial_sum += dial.index(j)+3 #다이얼이 3번은 무조건 돌려야해서 +3
print(dial_sum)



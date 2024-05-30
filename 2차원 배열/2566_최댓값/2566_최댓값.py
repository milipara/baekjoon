import sys

sys.stdin = open("2566_최댓값.txt")

A = [] #빈 배열 만들기
for i in range(9):
    A.append(list(map(int,input().split()))) #
row = 0 #열
col = 0 #행
max_val=0 #최대치 변수

for X in range(9): # X축 반복
    for Y in range(9): # Y축 반복
        if A[X][Y] >= max_val: # 최대치랑 X,Y축과 비교
            max_val = A[X][Y] # 그렇다면 X,Y축 숫자로 변경 그리고 X,Y축 입력
            row = X+1
            col = Y+1
print(max_val)
print(row,col)
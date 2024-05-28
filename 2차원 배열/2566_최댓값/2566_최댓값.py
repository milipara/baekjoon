import sys

sys.stdin = open("2566_최댓값.txt")

A = []
for i in range(9):
    A.append(list(map(int,input().split())))
row = 0
col = 0

for i in range(N):
    i = list(map(int,input().split())) # A배열에 append로 쌓기
    A.append(i)

for j in range(N):
    j = list(map(int,input().split())) # B배열에 append로 쌓기
    B.append(j)

for k in range(N):
    for l in range(M):
        print(A[k][l] + B[k][l], end= ' ')
    print()
import sys

sys.stdin = open("2738_행렬 덧셈.txt")

N , M = map(int,input().split())
A , B = [],[]

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
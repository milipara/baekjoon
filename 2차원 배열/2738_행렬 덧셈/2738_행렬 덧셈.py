import sys

sys.stdin = open("2738_행렬 덧셈.txt")

N , M = map(int,input().split())
A , B = [],[]

for i in range(N):
    a = list(map(int,input().split()))
    A.append(a)

for j in range(N):
    b = list(map(int,input().split()))
    B.append(b)

for k in range(N):
    for l in range(M):
        print([k][l] + B[k][l], end= ' ')
    print()
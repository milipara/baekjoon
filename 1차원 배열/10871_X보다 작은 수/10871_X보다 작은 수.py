import sys

sys.stdin = open("10871_X보다 작은 수.txt")

# n = int(input())
N , X = map(int,(input().split()))
A = list(map(int,(input().split())))

for N2 in range(1,N):
    if A[N2] <= X:
        print(A[N2], end=" ")

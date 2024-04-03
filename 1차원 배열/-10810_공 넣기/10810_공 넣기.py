import sys

sys.stdin = open("10810_공 넣기.txt")

# n = int(input())
N , M = map(int,(input().split()))
basket = [0] * (N+1)

for N2 in range(M):
    i , j , k = map(int, (input().split()))
    for N3 in range(i,j+1):
        basket[N3] = k;

for i in range(1,N+1):
    print(basket[i], end=" ")
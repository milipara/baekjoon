import sys

sys.stdin = open("10810_공 넣기.txt")

# n = int(input())
N , M = map(int,(input().split()))
basket = [0] * (N+1) # 바구니 설치

for N2 in range(0,M): #공 넣는 텀
    i , j , k = map(int, (input().split())) # i~j까지 k개 넣기
    for N3 in range(i,j+1):
        basket[N3] = k;

for i in range(1,N+1): # 공 넣은 텀 모두 합치기
    print(basket[i], end=" ")
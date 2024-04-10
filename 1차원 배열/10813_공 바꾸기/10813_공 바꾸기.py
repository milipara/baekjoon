import sys

sys.stdin = open("10813_공 바꾸기.txt")

# n = int(input())
N , M = map(int,(input().split()))
basket = [i for i in range(1,N+1)]#[0] * (N+1) # 바구니 설치
change_basket = 0;

for N2 in range(M): #공 넣는 텀
    i , j = map(int, (input().split())) # i~j까지 k개 넣기
    change_basket = basket[i-1]
    basket[i-1] = basket[j-1]
    basket[j-1] = change_basket;

for i in range(N): # 공 넣은 텀 모두 합치기
    print(basket[i], end=" ")
import sys

sys.stdin = open("10813_공 바꾸기.txt")

# n = int(input())
N , M = list(map(int,(input().split())))
basket = [i for i in range(1,N+1)] # 바구니 설치
change_basket = 0; # 바꾸는 바구니 더미데이터

for N2 in range(M): #공 바꾸는 횟 수
    i , j = map(int, (input().split())) # 바꾸는 바구니 2개 i ,j를 설정
    change_basket = basket[i-1]
    basket[i-1] = basket[j-1]
    basket[j-1] = change_basket;

for i in range(0,N): # 바꾼 바구니 나렬
    print(basket[i], end=" ")
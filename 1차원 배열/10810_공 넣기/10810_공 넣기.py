import sys

sys.stdin = open("10810_공 넣기.txt")

# n = int(input())
N , M = map(int,(input().split()))

for N2 in range(1,M+1):
    i , j , k = list(map(int, (input().split())))

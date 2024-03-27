import sys

sys.stdin = open("15552_빠른 A+B.txt")

# n = int(input())
T = int(input())

for N in range(1,T+1):
    A , B = map(int,input().split())
    print(A+B);
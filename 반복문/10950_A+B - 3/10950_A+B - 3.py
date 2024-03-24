import sys

sys.stdin = open("10950_A+B - 3.txt")

# n = int(input())
T = int(input())

for N in range(1,T+1):
    A , B = map(int,input().split())
    print(A+B);
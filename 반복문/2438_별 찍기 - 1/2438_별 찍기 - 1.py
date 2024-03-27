import sys

sys.stdin = open("2438_별 찍기 - 1.txt")

# n = int(input())
N = int(input())

for N2 in range(1,N+1):
    print("*"*N2);
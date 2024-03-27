import sys

sys.stdin = open("2439_별 찍기 - 2.txt")

# n = int(input())
N = int(input())

for N2 in range(1,N+1):
    print(" "*(5-N2)+"*"*N2);
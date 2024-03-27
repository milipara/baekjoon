import sys

sys.stdin = open("11021_A+B - 7.txt")

# n = int(input())
T = int(input())

for N in range(1,T+1):
    A , B = map(int,input().split())
    print("case #"+str(N)+": "+str(A+B));
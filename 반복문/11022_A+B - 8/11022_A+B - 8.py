import sys

sys.stdin = open("11022_A+B - 8.txt")

# n = int(input())
T = int(input())

for N in range(1,T+1):
    A , B = map(int,input().split())
    print("case #"+str(N)+": "+str(A)+" + "+str(B)+" = "+str(A+B))
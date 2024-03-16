import sys

sys.stdin = open("1001_A-B.txt")

# n = int(input())
A, B = list(map(int,input().split()));

print(A-B);
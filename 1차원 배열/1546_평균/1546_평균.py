import sys

sys.stdin = open("1546_평균.txt")

n = int(input())
MATH = list(map(int,input().split()))
M = max(MATH)

for i in range(n):
    MATH[i] = MATH[i]/M*100
print(sum(MATH)/n)
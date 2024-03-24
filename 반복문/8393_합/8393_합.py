import sys

sys.stdin = open("8393_합.txt")

# n = int(input())
N = int(input());
num=0;
for N2 in range(1,N+1):
    num += N2
print(num)
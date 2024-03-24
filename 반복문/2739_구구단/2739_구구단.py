import sys

sys.stdin = open("2739_구구단.txt")

# n = int(input())
N = int(input())

for N2 in range(1,10):
    print(N," * ",N2," = ",N * N2);
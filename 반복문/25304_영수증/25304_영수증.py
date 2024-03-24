import sys

sys.stdin = open("25304_영수증.txt")

X = int(input());
N = int(input());
num = 0;

for N2 in range(1,N+1):
    a , b = map(int,input().split())
    num += a * b
if X == num:
    print("Yes")
else:
    print("No")

X = int(input());
N = int(input());
num = 0;

for N2 in range(1,N+1):
    a , b = map(int,input().split())
    num += a * b
if X == num:
    print("Yes")
else:
    print("No")
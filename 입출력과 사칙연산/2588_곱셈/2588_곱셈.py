import sys

sys.stdin = open("2588_곱셈.txt")

# n = int(input())
A = int(input());
B = input();

print(A*int(B[2]));
print(A*int(B[1]));
print(A*int(B[0]));
print(A*int(B));
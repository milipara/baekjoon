import sys

sys.stdin = open("10869_사칙연산.txt")

# n = int(input())
A, B  = list(map(int,input().split()));

print(A+B);
print(A-B);
print(A*B);
print(int(A/B));
print(A%B);
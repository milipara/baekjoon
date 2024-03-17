import sys

sys.stdin = open("10430_나머지.txt")

# n = int(input())
A, B, C = list(map(int,input().split()));

print((A+B)%C);
print(((A%C) + (B%C))%C);
print((A*B)%C);
print(((A%C)*(B%C))%C);

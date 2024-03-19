import sys

sys.stdin = open("1330_두 수 비교하기.txt")

# n = int(input())
A, B = map(int,input().split());

if A > B:
    print(">")
elif A < B:
    print("<")
else:
    print("==")

A, B = map(int,input().split());

if A > B:
    print(">")
elif A < B:
    print("<")
else:
    print("==")

A, B = map(int,input().split());

if A > B:
    print(">")
elif A < B:
    print("<")
else:
    print("==")
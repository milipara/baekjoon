import sys

sys.stdin = open("10988_팰린드롬인지 확인하기.txt")

S = input()
if S == S[::-1]:
    print("1")
else:
    print("0")

S = input()
if S == S[::-1]:
    print("1")
else:
    print("0")
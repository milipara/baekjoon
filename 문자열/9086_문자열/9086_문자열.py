import sys

sys.stdin = open("9086_문자열.txt")

T = int(input())
for test_case in range(T):
    S = input()
    print(S[0],S[-1])
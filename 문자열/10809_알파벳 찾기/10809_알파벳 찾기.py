import sys

sys.stdin = open("10809_알파벳 찾기.txt")

S = input()
check="abcdefghijklmnopqrstuvwxyz"

for i in check:
    print(S.find(i), end=" ")
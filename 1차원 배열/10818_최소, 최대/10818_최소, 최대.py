import sys

sys.stdin = open("10818_최소, 최대.txt")

# n = int(input())
N = int(input())
LIST = list(map(int,input().split()));
print(min(LIST),max(LIST))
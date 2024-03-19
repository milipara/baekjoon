import sys

sys.stdin = open("2753_윤년.txt")

# n = int(input())
num = int(input())

if (num % 4 == 0) and (num % 100 != 0 or num % 400 == 0):
    print("1")
else:
    print("0")

num = int(input())

if (num % 4 == 0) and (num % 100 != 0 or num % 400 == 0):
    print("1")
else:
    print("0")
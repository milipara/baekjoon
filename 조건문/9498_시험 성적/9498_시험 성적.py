import sys

sys.stdin = open("9498_시험 성적.txt")

# n = int(input())
num = int(input())

if num >= 90:
    print("A")
elif num >= 80:
    print("B")
elif num >= 70:
    print("C")
elif num >= 60:
    print("D")
else:
    print("F")
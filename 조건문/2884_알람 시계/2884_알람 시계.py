import sys

sys.stdin = open("2884_알람 시계.txt")

# n = int(input())
H , M = map(int,input().split())

if M < 45:
    if H == 0:
        H=23
        M+=60
    else:
        H -= 1
        M += 60
print(H , M-45)

H , M = map(int,input().split())

if M < 45:
    if H == 0:
        H=23
        M+=60
    else:
        H -= 1
        M += 60
print(H , M-45)

H , M = map(int,input().split())

if M < 45:
    if H == 0:
        H=23
        M+=60
    else:
        H -= 1
        M += 60
print(H , M-45)
import sys

sys.stdin = open("2525_오븐 시계.txt")

# n = int(input())
H , M = map(int,input().split())
M2 = int(input())

H += M2//60 # 몫만 가져와서 시간 계산
M += M2 % 60 #나머지로 분 계산

if M >= 60:
    H += 1
    M -= 60
if H >= 24:
    H -= 24
print(H,M)

H , M = map(int,input().split())
M2 = int(input())

H += M2//60
M += M2 % 60

if M >= 60:
    H += 1
    M -= 60
if H >= 24:
    H -= 24
print(H,M)

H , M = map(int,input().split())
M2 = int(input())

H += M2//60
M += M2 % 60

if M >= 60:
    H += 1
    M -= 60
if H >= 24:
    H -= 24
print(H,M)
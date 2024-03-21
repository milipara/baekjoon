import sys

sys.stdin = open("2480_주사위 세개.txt")

# n = int(input())
n1 , n2 , n3 = map(int,input().split())

if n1 == n2 == n3:
    print(10000 + n1*1000)
elif (n1 == n2) or (n1 == n3) :
    print(1000 + n1 * 100)
elif (n2 == n3):
    print(10000 + n2 * 1000)
else:
    print(max(n1,n2,n3)*100)

n1 , n2 , n3 = map(int,input().split())

if n1 == n2 == n3:
    print(10000 + n1*1000)
elif (n1 == n2) or (n1 == n3):
    print(1000 + n1 * 100)
elif (n2 == n3):
    print(10000 + n2 * 1000)
else:
    print(max(n1,n2,n3)*100)

n1 , n2 , n3 = map(int,input().split())

if n1 == n2 == n3:
    print(10000 + n1*1000)
elif (n1 == n2) or (n1 == n3):
    print(1000 + n1 * 100)
elif (n2 == n3):
    print(10000 + n2 * 1000)
else:
    print(max(n1,n2,n3)*100)

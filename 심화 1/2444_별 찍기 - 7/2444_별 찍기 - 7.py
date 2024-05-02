import sys

sys.stdin = open("2444_별 찍기 - 7.txt")

N=int(input())
for i in range(1,N+1):
    print(" "*(5-i),"*"*(i+(i-1)))
for i in range(N,0,-1):
    print(" "*(5-i),"*"*(i+(i-1)))
import sys

sys.stdin = open("2675_문자열 반복.txt")

test_case = int(input())

for i in range(test_case):
    N , S = input().split()
    N = int(N)#숫자로 변환
    S = str(S)#문자로 변환

    for i in range(len(S)): #문자 길이만큼 반복
        print(S[i]*N,end='')#각 문자마다 N회 반복
    print() #줄바꿈
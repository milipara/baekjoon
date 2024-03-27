import sys

sys.stdin = open("10951_A+B - 4.txt")

# n = int(input())
while True:
    try: # 가져올 수 있을 때까지 반복
        A , B = map(int,input().split())
        print(A + B);
    except: # 가져올 수가 없을 시 빠져나간다.
        break;


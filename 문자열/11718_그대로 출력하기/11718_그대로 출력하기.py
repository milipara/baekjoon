import sys

sys.stdin = open("11718_그대로 출력하기.txt")

while True: #가능할때까지 반복
    try:
        print(input()) #문자 가져오기
    except EOFError: #에러 날시
        break; #빠져나가기

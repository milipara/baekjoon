import sys

sys.stdin = open("1316_그룹 단어 체커.txt")

test_case = int(input())
N = test_case

for i in range(test_case):
    word = input()
    for j in range(len(word)-1): #문자길이 만큼 반복
        if word[j] == word[j+1]: #j+1까지 비교 맞다면 넘기기
            pass
        elif word[j] in word[j+1:]: # j+1 부터 끝까지 비교 맞다면 N카운터에서 1개 빼기
            N-=1
            break
print(N)

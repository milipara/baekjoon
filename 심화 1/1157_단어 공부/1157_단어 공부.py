import sys

sys.stdin = open("1157_단어 공부.txt")

word=[]#빈 리스트
S = input().upper()#대문자로 출력
S_word=set(S)#중복된 단어 삭제

for i in S_word: # 중복단어 삭제한 단어만큼 반복
    count = S.count(i) #알파벳 갯수만큼 카운터
    word.append(count) # 빈 리스트에 입력

if word.count(max(word))>=2: # 문자열이 2개이상 일 경우 ? 출력
    print("?")
else: # 아닐 경우 문자열에서 가장 높은 숫자 인덱스를 찾아 넣는다.
    print(S_word[word.index(max(word))])
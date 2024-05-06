import sys

sys.stdin = open("1157_단어 공부.txt")

word={}
S = input()
for i in len(S):
    if i in word:
        word[i]+=1
    else:
        word[i]=1
print(len(S))
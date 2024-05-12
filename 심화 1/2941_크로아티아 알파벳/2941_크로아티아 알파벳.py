import sys

sys.stdin = open("2941_크로아티아 알파벳.txt")

croatia = ['c=','c-','dz=','d-','lj','nj','s=','z=']
S = input()
for i in croatia:
    S = S.replace(i,"*") # S에 있는 문자를 크로아티아 목록에 있으면 *로 변경
print(len(S)) # S길이를 출력

S = input()
for i in croatia:
    S = S.replace(i, "*")  # S에 있는 문자를 크로아티아 목록에 있으면 *로 변경
print(len(S))  # S길이를 출력

S = input()
for i in croatia:
    S = S.replace(i, "*")  # S에 있는 문자를 크로아티아 목록에 있으면 *로 변경
print(len(S))  # S길이를 출력

S = input()
for i in croatia:
    S = S.replace(i, "*")  # S에 있는 문자를 크로아티아 목록에 있으면 *로 변경
print(len(S))  # S길이를 출력

S = input()
for i in croatia:
    S = S.replace(i, "*")  # S에 있는 문자를 크로아티아 목록에 있으면 *로 변경
print(len(S))  # S길이를 출력
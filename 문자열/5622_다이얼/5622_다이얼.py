import sys

sys.stdin = open("5622_다이얼.txt")

dial=["ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]
S = input()
print(S)
dial_sum=0;
for i in range(len(S)):
    for j in dial:
        if S[i] in j:
            dial_sum += dial.index(j)+3
print(dial_sum)



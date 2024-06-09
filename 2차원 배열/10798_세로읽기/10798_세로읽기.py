import sys

sys.stdin = open("10798_세로읽기.txt")

words = []
list = ""
num=[]
for i in range(5):
    word=input()
    words.append(word)
    num.append(len(word))

for i in range(num):
    for j in range(5):
        list += words[j][i]
print(list)
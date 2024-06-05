import sys

sys.stdin = open("10798_세로읽기.txt")

words = []
list = ""
for i in range(5):
    word=input()
    words.append(word)

for i in range(5):
    for j in range(5):
        list += words[i][j]
print(list)
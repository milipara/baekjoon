import sys

sys.stdin = open("10798_세로읽기.txt")

words = []
for i in range(5):
    word=input()
    words.append(word)

print(words)
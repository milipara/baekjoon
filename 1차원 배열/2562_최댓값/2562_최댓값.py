import sys

sys.stdin = open("2562_최댓값.txt")

# n = int(input())
LIST = [];
for i in range(1, 10):
    LIST.append(int(input()));

print(max(LIST))
print(LIST.index(max(LIST))+1)
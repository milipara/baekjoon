import sys

sys.stdin = open("14681_사분면 고르기.txt")

# n = int(input())
x = int(input());
y = int(input());

if x>0 and y>0:
    print("1")
elif x<0 and y>0:
    print("2")
elif x<0 and y<0:
    print("3")
elif x>0 and y<0:
    print("4")

x = int(input());
y = int(input());

if x>0 and y>0:
    print("1")
elif x<0 and y>0:
    print("2")
elif x<0 and y<0:
    print("3")
elif x>0 and y<0:
    print("4")
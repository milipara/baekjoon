import sys

sys.stdin = open("3052_나머지.txt")

# n = int(input())
num_list = []
for N2 in range(10): #숫자 10개를 받는다.
    num = int(input())
    num_list.append(num % 42) #42로 나눈 나머지를 num_list에 넣는다.
num_list=set(num_list) #중복은 제거한다.
print(len(num_list))
num_list = []
for N2 in range(10): #숫자 10개를 받는다.
    num = int(input())
    num_list.append(num % 42) #42로 나눈 나머지를 num_list에 넣는다.
num_list=set(num_list)  #중복은 제거한다.
print(len(num_list))
num_list = []
for N2 in range(10): #숫자 10개를 받는다.
    num = int(input())
    num_list.append(num % 42) #42로 나눈 나머지를 num_list에 넣는다.
num_list=set(num_list)  #중복은 제거한다.
print(len(num_list))
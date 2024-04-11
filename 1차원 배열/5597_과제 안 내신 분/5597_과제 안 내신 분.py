import sys

sys.stdin = open("5597_과제 안 내신 분.txt")

# n = int(input())
student = [i for i in range(1,30+1)] # 학생 수 30명 뽑기

for N2 in range(28): #28명이 제출
    assignment = int(input())
    student.remove(assignment) # 28명 제거
student.sort() # 학생 정렬
for i in range(len(student)): # 학생 수 만큼만 출력
  print(student[i])
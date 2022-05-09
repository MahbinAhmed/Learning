# Link :- https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true

n = int(input("Enter student's number :- "))
student_mark = {}

for i in range(n):
    name, *points = input().split()
    marks = list(map(float,points))
    student_mark[name] = marks
query_input = input("Enter the student name :- ")

mark_list = student_mark.get(query_input)

a = 0
for i in mark_list:
    a = a+i

average = a/3

print("{:.2f}".format(average))
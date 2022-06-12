# Link :- https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true

def take_input():
    return list(input().split())

list1 = []

n = int(input("Enter total input number :- "))

for i in range(n):
    inp_list = take_input()
    if inp_list[0] == "insert":
        list1.insert(int(inp_list[1]),int(inp_list[2]))
    elif inp_list[0] == "print":
        print(list1)
    elif inp_list[0] == "append":
        list1.append(int(inp_list[1]))
    elif inp_list[0] == "sort":
        list1.sort()
    elif inp_list[0] == "pop":
        list1.pop()
    elif inp_list[0] == "reverse":
        list1.reverse()
    elif inp_list[0] == "remove":
        list1.remove(int(inp_list[1]))
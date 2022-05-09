# Link :- https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

# if __name__ == '__main__':
#     list1 = []
#     for i in range(int(input())):
#         name = input()
#         score = float(input())
#         a = [name,score]
#         list1.append(a)

#     for i in list1:
#         print(i[1])

score_list = {}
for _ in range(eval(input())):
    name = input()
    score = float(input())
    if score in score_list:
        score_list[score].append(name)
    else:
        score_list[score] = [name]
new_list = []
for i in score_list:
    new_list.append([i, score_list[i]])
new_list.sort()
result = new_list[1][1]
result.sort()
print (*result, sep = "\n")

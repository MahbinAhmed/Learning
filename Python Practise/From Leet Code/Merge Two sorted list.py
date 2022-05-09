# Link :- https://leetcode.com/problems/merge-two-sorted-lists/

list1 = [1,2,4]
list2 = [1,3,4]

for i in list2:
    list1.append(i)

list1.sort()
print(list1)
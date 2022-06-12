# Map
list1 = ["5","8","45","50"]
mapping=list(map(int,list1))

# for i in range(len(list1)):
#     list1[i]=int(list1[i])
mapping[2] = mapping[2]+5
# print(mapping[2])


list2 = [2,4,5,3,7]
def square(a):
    return a*a

def cube(a):
    return a*a*a
print_square=list(map(square,list2))
# print(print_square)

func = [square,cube]
for i in range(5):
    val = list(map(lambda x:x(i),func))
    # print(val)

# Filter

list3 = [1,2,3,4,5,6,7,8,9]
def is_grater_than_4(num):
    return num>4
greater_checking = list(filter(is_grater_than_4,list3))
# print(greater_checking)

#Reduce
from functools import reduce
list4 = [1,2,3,4,5,6,7,8,9]
num = reduce(lambda x,y:x+y, list4)
print(num)
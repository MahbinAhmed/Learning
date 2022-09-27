# print("abbas">"abbaox")

# list1 = ["John","Joe","Rick"]
# new_name = "Alex"
# a = 0
# for i in range(len(list1)):
#     if list1[i]>new_name:
#         list1.insert(i,new_name)
#         break

# print(list1)

# a = []
# b = [2,3]
# c = []
# d = a+b+c 
# print(d)

# print((0+1)//2)
# print(min([x for x in [None, 5, None] if x is not None]))

# print(abs(40-5))
# key = "Hey"
# value = "hello"
# list1 = [None,None,None,None,None]
# # list1[2] = key,value
# # print(list1[1])
# for j in range(5):
#     a = False
#     for i in range(5):
#         if i == 10:
#             print("Hello")
#             a  = True
#     if not a:
#         print("Hey")

# print("\"We Are One Family!\""
# )
# int(input().split())

# def charge_counter(per):
#     if per <= 60:
#         return (60-per)+40+60
#     elif per > 60 and per<=80:
#         return ((80-per)*2)+60
#     elif per > 80:
#         return (100-per)*3

# test_cases = int(input())
# input_list = []
# for i in range(test_cases):
#     user_input = input()
#     user_input = user_input.replace("%","")
#     user_input = int(user_input)
#     input_list.append(user_input) 

# for i in input_list:
#     result = charge_counter(i)
#     print(result, "minutes")

# user_input = 5
# for i in range(user_input+1):
#     print(" "*i, "*"*i)
# # print("*"*(user_input*2))
# # print("*"*(user_input*2))
# for i in range(user_input,0,-1):
#     print(reversed(" "*i,"*"*i))
#     # for j in range(user_input,0,-1):
#     #     print("*"*j)
# # for i in range(5):
# #     for j in range(5):
# #         print(" "*j, "*"*i)

# list1 = [5]
# list2 = [7]
# print(list1<list2)
# list1.insert(-1,4)
# print(list1)
# for i in range(len(list1)):
    # print(list1[i])
    # print(i)

# hey = {1,3,5}
# hey.

# list1 = [2,3,4,5]
# # list2 = [6,7,8,9]
# l = 2
# end = 3
# print(list1[l])
# list1[l],list1[end]=list1[end],list1[l]
# # print(l)
# # print(end)
# # print(list1)
# print(list1[l])

# def something(list,a):
#     list.pop()
#     return 0

# list = [1,2,4]
# b = something(list,1)
# print(b)
# print(list)

# dictionary = {("Hello","Guys"):0}
# key=(5,5)
# dictionary[key]=0
# print(dictionary[("Hello","Guys")])

# def func():
#     # dict1 = {}
#     a = 1
#     def hello():
#         # dict1["Hi"] = "Hello"
#         # print(dict1)
#         a = 2
#         return 0
#     print(a)
#     # return hello()

# print(func())
# def something(n):
#     s = len(n)
#     for i in range(s):
#         print(i)

# something([5,4,5,3,5])
# edges = [(1,4),(0,2,),(1,3),(4,2),(1,2),(0,3)]
# # for i,j in edges:
# #     print(f"i:{i}, j:{j}")

# bl_list = [[] for _ in range(5)]
# # print(bl_list)
# for i,j in edges:
#     bl_list[i].append(j)
#     bl_list[j].append(i)

# print(bl_list)

# list2 = ["Hello","Hi"]
# print()
# list1 = [["Hello","Hi"],["Helloooo","Hii"]]
# print(list1, end="\n\n")


# l = [False,False,False]
# for i in range(3):
#     if i not in l:
# #         print("Hello")\
# stack = [[0,1,1],[0,15,41],[4,13,14],[0,231,15]]
# # a = stack.pop()
# # stack.append(1)
# # print(stack)
# # print(type(a))
# # for i in stack:
# #     j,k,l = i
# #     print("j",j)
# #     print("k",k)
# #     print("l",l)

# print(float("inf")>45)


# class Graph_with_dir_and_wgt():
#     def __init__(self,num_nodes,nodes,weighted=False,directed=False) -> None:
#         self.num_nodes = num_nodes
#         self.weighted = weighted
#         self.directed = directed
#         self.nodes = nodes
#         self.routes = [[] for _ in range(self.num_nodes)]
#         self.weights = [[] for _ in range(self.num_nodes)]
#         for i in self.nodes:
#             if self.weighted:
#                 j,k,l = i
#                 self.routes[j].append(k)
#                 self.weights[j].append(l)
#                 if not directed:
#                     self.routes[k].append(j)
#                     self.weights[k].append(l)
#             else:
#                 j,k = i
#                 self.routes[j].append(k)
#                 if not directed:
#                     self.routes[k].append(j)
#     def weight(self,first,second=None):
#         weights = self.weights[first]
#         # print(weights)
#         # print(list(zip(self.routes,self.weights)))
#         index = self.routes[1].index(4)
#         print(self.weights[1][index])
#     def __repr__(self) -> str:
#         result = []
#         if self.weighted:
#             for i,(routes,weights) in enumerate(zip(self.routes,self.weights)):
#                 result.append(f"node |{i}| : routes-{routes}, weight-{weights}")
#         else:
#             for i,j in enumerate(self.routes):
#                 result.append(f"node |{i}| : routes-{routes}")
#         return "\n".join(result)

#     def __str__(self) -> str:
#         return self.__repr__()

# g2 = Graph_with_dir_and_wgt(5,[[0,1,2],[0,4,4],[1,4,8],[1,3,1],[2,1,7],[3,4,5],[3,2,6],[4,3,5]],weighted=True,directed=True)
# # print(g2)
# print(g2.weight(0))

# def diagonalDifference(arr:list):
#     arr.pop(0)
#     left_idx = 0
#     right_idx = len(arr)-1
#     left_to_right = 0
#     right_to_left = 0
#     for i in arr:
#         left_to_right = left_to_right+i[left_idx]
#         right_to_left = right_to_left+i[right_idx]
#         left_idx += 1
#         right_idx -= 1
#     return abs(left_to_right-right_to_left)

# print(diagonalDifference([3,[11,2,4],[4,5,6],[10,8,-12]]))

# def sum_ineff(array):
#     result = 0
#     if len(array)==3:
#         reuslt = result+array[0]+array[1]+array[2]
    
#     return result

# print(sum_ineff([1,2,3]))
# if 20 in range(6,20):
#     print("Hello")

    # list1 = [None,None,None,None,None]
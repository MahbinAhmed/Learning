# Link :- https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true

# list1 = [1,2,3,4,5]

# a = max(list1)

# list1.remove(a)
# print(list1)
# print(max(list1))

# length_input = int(input("Enter the list length :- "))

# score_list = []

# for i in range(length_input):
#     a = int(input("Enter the number :- "))
#     score_list.append(a)

# print(score_list)

# if __name__ == '__main__':
#     n = int(input())
#     score_list = set()
    
#     for i in range(n):
#         a = int(input())
#         score_list.add(a)
        
#     first_max = max(score_list)
#     score_list.remove(first_max)
#     print("Output :- ", max(score_list))

#     # print(score_list)

# if __name__ == '__main__':
#     n = int(input())
#     score_list = set()
    
#     string_input = input()
#     a = string_input.split(" ")

#     if len(a) == n:

#         for i in a:
#             score_list.add(i)
            
#         first_max = max(score_list)
#         score_list.remove(first_max)
#         print("Output :- ", max(score_list))

#     else:
#         print(f"Enter {n} number of items.")

# #     # print(score_list)




# if __name__ == '__main__':
#     n = int(input())
#     arr = map(int, input().split())
#     m1 = max(arr)
#     m2 = -9999999999
#     for i in range(n):
#         if arr[i] != m1 and arr[i] > m2:
#             m2 = arr[i]
#     print(m2)

# Final

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    m1 = max(arr)
    m2 = -9999999999
    for i in range(n):
        if arr[i] != m1 and arr[i] > m2:
            m2 = arr[i]
    print(m2)

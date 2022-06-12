# list1 = list(map(int, input().split()))
# print(list1)

# a,b = list(map(int,input().split()))
# print(a+b)

# number = "{:3}".format(50000)
# print(number)
# text = "Hello"
# print("".join(list(reversed(text))))

# S = input()
# if "".join(list(reversed(S))) == S:
# 	print("Yes")
# else:
# 	print("No")

# list1 = input().split()
# print(list1)

# def divisor(n):
#     div_list = []
#     for i in range(1,n+1):
#         if n%i==0:
#             div_list.append(i)
#     return div_list

# divisor_list = divisor(6)
# for i in divisor_list:
#     print(i)

# def is_prime(n):
#     for i in range(2,n):
#         if n%i==0:
#             return False
#     else:
#         return True

# user_input = int(input())
# if is_prime(user_input):
#     print("NO PUNISHMENT")
# else:
#     for _ in range(user_input):
#         print("I DID NOT DO THE ASSIGNMENT.")

# string = "ababa"

# print(string.count("aba"))

def is_prime(n):
    list1 = []
    for i in range(2,n):
        if n%i==0:
            list1.append(i)
        else:
            pass
    return list1

def is_cprime(n,m):
    list_of_n = is_prime(n)
    list_of_m = is_prime(m)
    for i in list_of_n:
        for j in list_of_m:
            if i==j:
                return "This pair is not co-prime"
    return "This pair is co-prime"

a,b = list(map(int, input("Enter your pair (With a space) :- ").split()))

print(is_cprime(a,b))
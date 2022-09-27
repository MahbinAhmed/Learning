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

# def is_prime(n):
#     list1 = []
#     for i in range(2,n):
#         if n%i==0:
#             list1.append(i)
#         else:
#             pass
#     return list1

# def is_cprime(n,m):
#     list_of_n = is_prime(n)
#     list_of_m = is_prime(m)
#     for i in list_of_n:
#         for j in list_of_m:
#             if i==j:
#                 return "This pair is not co-prime"
#     return "This pair is co-prime"

# a,b = list(map(int, input("Enter your pair (With a space) :- ").split()))

# print(is_cprime(a,b))

# def factorial(n):
#     if n==1:
#         return 1
#     else:
#         return factorial(n-1) * n

# print(factorial(5))

import re


text = '''
Hey there !
I'm john 
SAVE MORE ON APP SELL ON DARAZ CUSTOMER CARE
 TRACK MY ORDER




 MAHBIN AHMED'S ACCOUNT
 ভাষা
 
Search in Daraz
SEARCH
 36Voucher
Categories
4 ITEMSPRICEQUANTITY
Package 1 of 3Shipped byMD Shahriar Kabir
Delivery Option



item
BATTERY CASE / HOLDER 18650
No Brand, Color Family:BATTERY CASE / HOLDER 18650
৳ 22

৳ 27

-19%

Qty: 2
Package 2 of 3Shipped byInfinite Store
Delivery Option



item
Digital Multimeter Volts Amps Resistors Ohms Tester VC9205A
No Brand, Color Family:Black
৳ 384

৳ 650

-41%

Qty: 1
Package 3 of 3Shipped bySujon
Delivery Option



item
2 Pieces 2000mAh-2200mAh 3.7Volt Battery (These are opened from the laptop battery Pack), Capacity Tested, Authentic Products, Different Brands
No Brand
৳ 180

Qty: 1
Proceed to Pay
Shipping & Billing

Mahbin AhmedEDIT
COLLECTION POINTDEX SHERPUR STATION Khowarpar Shapla Chattar,Sonar Bangla Bus Stand Road, West Gauripur, Sherpur Town, Sherpur (Old Nayantari Eye Hospital Building), Sherpur Shadar, Sherpur, Mymensingh
Bill to default billing addressEDIT
1705358924
EDIT
mahbinahmed10@gmail.com
EDIT
Order Summary
Subtotal (4 Items)
৳ 608
Shipping Fee
৳ 210
Shipping Fee Discount
-৳ 195
Daraz vouchers
-৳ 30
Enter Voucher Code
 	APPLY
Total:	৳ 593
VAT included, where applicable
Proceed to Pay
Customer Care
Help Center
How to Buy
Returns & Refunds
Contact Us
Terms & Conditions
Earn With Daraz
Daraz University
Sell on Daraz
Code of Conduct
Join the Daraz Affiliate Program
Daraz
About Daraz
Digital Payments
Careers
Daraz Blog
Daraz Cares
dMart
Privacy Policy
Daraz App
Daraz Exclusives
Hungrynaki Food Delivery
BD Cricket Live
Soybean Oil


Happy Shopping
Download App

'''

# regex_pattern = r"d\w+"
# print(re.findall(regex_pattern,text))

dict1 = {"Hello":6,"Hi":5}
print(dict1.get("Hello"))
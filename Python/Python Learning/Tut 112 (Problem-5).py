# Problem-5

# Function_section
def next_palindrome(a):
    a += 1
    while not is_palindrome(a):
        a += 1
    return a

def is_palindrome(a):
    return str(a) == str(a)[::-1]

# List_section
list = [1,5,20,60,87]

# Processing_unit
for i in list:
    if i>10:
        print(f"The palindrome for {i} is {next_palindrome(i)}")
    elif i==10:
        print(f"The number is 10")
    else :
        print(f"The number is less than 10")
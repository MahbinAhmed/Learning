# Link :- https://www.hackerrank.com/challenges/write-a-function/problem?isFullScreen=true

def leap_year_checker(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Taking Input from the user
input = int(input("Enter the year you want check :- "))

checker = leap_year_checker(input)

if checker==True:
    print("Yes. This is a leap year !")
else:
    print("No. This is not a leap year !")
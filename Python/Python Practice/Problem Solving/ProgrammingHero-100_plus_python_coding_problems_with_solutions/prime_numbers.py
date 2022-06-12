# Problem
# Ask the user to enter a number. Then find all the primes up to that number.

def prime_checker(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

def all_prime(n):
    prime_list = []
    for i in range(2,n+1):
        if prime_checker(i) == True:
            prime_list.append(i)
    return prime_list

upper_limit = int(input("Enter your upper limit:- "))
all_primes = all_prime(upper_limit)
print(all_primes)
import time
from functools import lru_cache

@lru_cache(maxsize=2)
def sleeper(n):
    time.sleep(n)
    return n

print("First print")
sleeper(5)
print("Second print")
sleeper(3)
print("Third print")
sleeper(4)
print("Fourth print")
sleeper(4)
print("Fifth print")
sleeper(4)
print("Sixth print")
sleeper(4)
print("Seventh print")

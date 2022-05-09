# Cache Module

from functools import lru_cache
import time

@lru_cache(maxsize=5)
def function(a):
    time.sleep(a)
    return "Called."

print("First time calling...")
print(function(3))
print("Calling again...")
print(function(3))
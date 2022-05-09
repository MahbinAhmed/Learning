# Function Caching

from functools import lru_cache
import time

@lru_cache()
def function(n):
    time.sleep(n)
    return n

print("Calling...")
function(3)
function(2)
function(1)
print("Calling again....")
function(3)
print("Called")
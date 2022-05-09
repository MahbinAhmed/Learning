# a = iter("Hello")
# print(a.__next__())
# print(a.__next__())

def gen():
    for i in range(10):
        yield i


c = gen()
print(c.__next__())
print(c.__next__())
# list = []
#
# for i in range(100):
#     if i%3==0:
#         list.append(i)

# list = [i for i in range (100) if i%3==0]
#
# print(list)

# dict = {0:"Item0",1:"Item1",2:"Item2",3:"Item3",4:"Item4",5:"Item5"}

# dict = {i:f"Item {i}" for i in range (6) }
#
# print(dict)

# Book = {book for book in ["Book1","Book2","Book1","Book2"]}

# print(Book)

gen = (i for i in range(100))

print(gen.__next__())
for i in gen:
    print(i)
MAX_HASH_TABLE_SIZE = 4096

# CLASS WITHOUT COLLISION SOLVING --->>>
# class HashTable:
#     def __init__(self,max_size=4096) -> None:
#         self.list = [None]*max_size
#     def insert(self,key,value):
#         index = HashTable.get_index(self.list,key)
#         self.list[index] = (key,value)
#     @staticmethod
#     def get_index(list,key):
#         hash_number = 0
#         for i in key:
#             hash_number += ord(i)
#         result = hash_number % len(list)
#         return result
#     def find(self,key):
#         index = HashTable.get_index(self.list,key)
#         value = self.list[index][1]
#         if value is None:
#             return None
#         return value

#     def update(self,key,value):
#         index = HashTable.get_index(self.list,key)
#         self.list[index] = (key,value)
#     def list_all(self):
#         return [kv[0] for kv in self.list if kv is not None]
#     def deleter(self,key):
#         index = HashTable.get_index(self.list,key)
#         self.list[index] = None

# a = HashTable(500)
# # print(a.get_index("a"))
# a.insert("Hello","Hi")
# print(a.find("Hello"))
# print(a.list_all())
# data = [None]*60
# print(a.get_index(data,"Hello"))
# a.deleter("Hello")
# print(a.list_all())

# CLASS WITH COLLISION SOLVING --->>>
# class AdvanceHashTable():
#     def __init__(self,max_size=4096) -> None:
#         self.list = [None]*max_size
#     @staticmethod
#     def get_index(list,key):
#         hash_numebr = 0
#         for i in key:
#             hash_numebr += ord(i)
#         result = hash_numebr%len(list)
#         return result
#     @staticmethod
#     def valid_index(list,key):
#         index = AdvanceHashTable.get_index(list,key)
#         while True:
#             kv = list[index]
#             if list[index]==None:
#                 return index
#             k,v = kv
#             if key==k:
#                 return index
#             index += 1
#             if index == len(list):
#                 index = 0
#     def insert(self,key,value):
#         index = AdvanceHashTable.valid_index(self.list,key)
#         self.list[index] = (key,value)
#     def find(self,key):
#         index = AdvanceHashTable.valid_index(self.list,key)
#         value = self.list[index][1]
#         if self.list[index]is None:
#             return None
#         return value
#     def update(self,key,value):
#         index = AdvanceHashTable.valid_index(self.list,key)
#         self.list[index]=(key,value)
#     def list_all(self):
#         return [kv[0] for kv in self.list if kv is not None]
#     def deleter(self,key):
#         index = AdvanceHashTable.valid_index(self.list,key)
#         self.list[index] = None

# b = AdvanceHashTable(5000)
# b.insert("Hey","Guys")
# b.update("Hey","Hi")
# print(b.list_all())
# print(b.find("Hey"))
# b.deleter("Hey")
# print(b.list_all())
# data = [None]*5000
# print(b.valid_index(data,"a"))

# PYTHON FRIENDLY CLASS --->>>
class AdvanceHashTable():
    def __init__(self,max_size=4096) -> None:
        self.list = [None]*max_size
    @staticmethod
    def get_index(list,key):
        # hash_number = hash(key)
        hash_number = 0
        for i in key:
            hash_number += ord(i)
        result = hash_number%len(list)
        return result
    @staticmethod
    def valid_index(list,key):
        index = AdvanceHashTable.get_index(list,key)
        while True:
            kv = list[index]
            if list[index]==None:
                return index
            k,v = kv
            if key==k:
                return index
            index += 1
            if index == len(list):
                index = 0
    def __setitem__(self,key,value):
        index = AdvanceHashTable.valid_index(self.list,key)
        self.list[index] = (key,value)
    def __getitem__(self,key):
        index = AdvanceHashTable.valid_index(self.list,key)
        value = self.list[index][1]
        if self.list[index]is None:
            return None
        return value
    def __repr__(self):
        # list = [kv[1] for kv in self.list if kv is not None]
        # for i in list:
        #     return_text = f"[{i}"
        list = [f"{kv[0]} : {kv[1]}" for kv in self.list if kv is not None]
        return str(list)
    def __str__(self):
        return repr(self)
    def __delitem__(self,key):
        index = AdvanceHashTable.valid_index(self.list,key)
        self.list[index] = None
data = [None]*500
b = AdvanceHashTable()
# print(b.get_index(data,"Hello"))
# print(b.valid_index(data,"Hello"))
b["Hello"]="Hi"
b["Hello"]="Hey"
b["World"]="Python"
# print(b["Hello"])
print(b)
import pickle

# Storing database
employee1 = {"Name":"Alex","Age":28,"Post":"Senior Software Engineer","Salary":150000}
employee2 = {"Name":"John","Age":25,"Post":"Junior Software Engineer","Salary":120000}

database = {"Employee1":employee1,"Employee2":employee2}

in_file_database = pickle.dumps(database) #---> To make database without creating a file

# with open("database.pkl","wb")as f:
#     pickle.dump(database,f)
#     print("Database Updated!")

# Accessing database
# with open("database.pkl","rb")as f:
#     # print(pickle.load(f))
#     # print("Database printed!")
#     a = pickle.load(f)
#     for i in a:
#         print(i, a[i])

# print(pickle.loads(in_file_database)) #---> To access from database which is not created in a file
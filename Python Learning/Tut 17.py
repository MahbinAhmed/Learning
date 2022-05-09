# list1 = ["Alex","Charles","Smith","David","Josef"]
# for item in list1:     # It's used to run "for" loop
#     print(item)
#
# list2 = [["Andrew",5],["Dicens",8],["Charlie",4]]
# for object,number in list2:
#     print(number,"is", object)

#Quiz
list3 = ["Computer",5,"Mobile",8,3,"Tablet","Play Station",9]

for number in list3:
    if str(number).isnumeric() and number>6:
        print(number)
# LINEAR SEARCH----->>>>>
# def locate_card(array,query):
#     index = 0
#     while True:
#         if len(array)>0:
#             if array[index] == query:
#                 return index
#             index += 1

#         if index == len(array):
#             return -1

# # sorted_list = [3,4,5,6,7,8,9]
# # sorted_list = [3,4,4,4,4,4,5,6,7,8,9]
# # sorted_list = []
# query = 8

# print(locate_card(sorted_list,query))


# def locate_card(array,query):
#     lo_index = 0
#     high_index = len(array)-1
#     while lo_index <= high_index:
#         mid_index = (lo_index+high_index) // 2
#         mid_number = array[mid_index]

#         if mid_number == query:
#             return mid_index
#         elif mid_number < query:
#             lo_index = mid_index + 1
#         elif mid_number > query:
#             high_index = mid_index - 1

#     return -1

# Smart version of this code----->>>>>

def location_tester(array, query, mid_index):
    mid_number = array[mid_index]
    if mid_number == query:
        if mid_index >= 0 and array[mid_index-1] == query:
            return "left"
        else:
            return "found"
    elif mid_number < query:
        return "right"
    else:
        return "left"

def locate_card(array,query):
    lo, high_index = 0, len(array)-1
    while lo <= high_index:
        mid_index = (lo+high_index) // 2
        result = location_tester(array,query,mid_index)

        if result == "found":
            return mid_index
        elif result == "left":
            high_index = mid_index-1
        elif result == "right":
            lo = mid_index + 1
    return -1

sorted_list = [3,4,5,6,7,8,9]
# sorted_list = [3,4,5,6,7,8,8,8,8,8,8,8,8,8,8,8,9]
# sorted_list = [3,4,5,6,6,6,6,6,6,6,6,6,7,7,7,7,7,7,7,7,7,7,7,8,8,8,8,8,8,8,8,8,8,8,9]
sorted_list = [3,4,4,4,4,4,5,6,6,6,6,6,7,8,9]
sorted_list = []
query = 8
print(locate_card(sorted_list,query))
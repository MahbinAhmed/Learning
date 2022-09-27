# Assignment-1
# IN LINEAR FORM----->>>>>

# def linear_rotate_counter(array):
#     for i in range(len(array)):
#         if i > 0 and array[i]< array[i-1]:
#             return i
#     else:
#         return 0

# # IN BINARY SEARCH ALGORITHM----->>>>>
# def binary_rotate_counter(array):
#     lo_index = 0
#     high_index = len(array)-1
#     while lo_index<=high_index:
#         mid_index = (lo_index+high_index)//2
#         mid_number = array[mid_index]
#         if mid_index>0 and mid_number<array[mid_index-1]:
#             return mid_index
#         elif mid_number>array[len(array)-1]:
#             lo_index = mid_index+1
#         elif mid_number<array[len(array)-1]:
#             high_index = mid_index-1
#         elif len(array)==1:
#             return 0

#     return 0



# Bonus question-1
# def generic_binary_search(array,mid_index):
#     mid_number = array[mid_index]
#     if mid_index>0 and mid_number<array[mid_index-1]:
#         return "found"
#     elif mid_number<array[len(array)-1]:
#         return "left"
#     elif mid_number>array[len(array)-1]:
#         return "right"
#     elif mid_index==0:
#         return "found"

# def binary_rotate_counter(array):
#     lo_index = 0
#     high_index = len(array)-1
#     while lo_index<=high_index:
#         mid_index = (lo_index+high_index) // 2
#         generic_result = generic_binary_search(array,mid_index)
#         if generic_result == "found":
#             return mid_index
#         elif generic_result == "right":
#             lo_index = mid_index+1
#         elif generic_result == "left":
#             high_index = mid_index-1
#         else:
#             raise "Error occured!"
#     return 0


# Bonus question-2
def generic_binary_search(array,mid_index):
    mid_number = array[mid_index]
    last_index = array[len(array)-1]
    if mid_index>0 and mid_number<last_index:
        if mid_number==array[mid_index-1]:
            return "left"
        return "found"
    elif mid_number<last_index:
        return "left"
    elif mid_number>last_index:
        return "right"
    elif mid_index==0:
        return "found"

def binary_rotate_counter(array):
    lo_index = 0
    high_index = len(array)-1
    while lo_index<=high_index:
        mid_index = (lo_index+high_index) // 2
        generic_result = generic_binary_search(array,mid_index)
        if generic_result == "found":
            return mid_index
        elif generic_result == "right":
            lo_index = mid_index+1
        elif generic_result == "left":
            high_index = mid_index-1
        else:
            raise "Error occured!"
    return 0
# Bonus question-3





# inputs = [8,9,10,1,2,3,4,5,6,7]
# inputs = [6,7,8,9,10,1,2,3]
# inputs = [1,2,3]
# inputs = [3,1,2]
# inputs = [2,3,1]
# inputs = [1,2,3]
# inputs = []
# inputs = [1]
# inputs = [4,4,5,5,5,6,6,6,1,2,3,3]
inputs = [3,3,3,3,1,2]

print(binary_rotate_counter(inputs))